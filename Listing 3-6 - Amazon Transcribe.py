import boto3
import json
import pandas as pd

def transcribe_all_files(bucket):
    # Erstellen eines S3-Clients
    s3 = boto3.client('s3')
    # Erstellen eines Transcribe-Clients
    transcribe = boto3.client(
        'transcribe',
        aws_access_key_id='ACCESS_KEY',
        aws_secret_access_key='SECRET_KEY',
        region_name='REGION'
    )

    objects = s3.list_objects(Bucket=bucket)['Contents'] # Auflisten aller Objekte im Bucket

    df = pd.DataFrame(columns=['file_name', 'transcript']) # Initialisieren des DataFrame zur Speicherung aller Transkripte

    for obj in objects:
        key = obj['Key']
        if not key.endswith('.wav'): # Überspringen von Objekten, die keine Endung mit .wav haben 
            continue
        language_code = 'de-DE' # Festlegen der Sprache der Audiodaten
        job_name = key # Festlegen des Jobnamens (als exakten Namen der hochgeladenen Datei)
        
        # Starten des Transkriptionsjobs
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            LanguageCode=language_code,
            Media={'MediaFileUri': f's3://{bucket}/{key}'},
            OutputBucketName=bucket
        )

        # Warten, bis der Job abgeschlossen ist
        while True:
            status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
            if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break

        # Wenn der Job erfolgreich abgeschlossen wurde, wird das Transkript abgerufen
        if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
            transcript_object = s3.get_object(Bucket=bucket, Key=f'{job_name}.json')
            transcript = transcript_object['Body'].read().decode('utf-8')

            data = json.loads(transcript)
            transcript_string = data['results']['transcripts'][0]['transcript']
            print(f'file_name: {job_name}\ntranscript: {transcript_string}' + '\n' + '='*100)

            # Erstellen eines neuen DataFrame für die verarbeitete Datei
            new_df = pd.DataFrame([[job_name, transcript_string]], columns=['file_name', 'transcript'])
            df = pd.concat([df, new_df], ignore_index=True)
        else:
            print('Der Transkriptionsauftrag ist fehlgeschlagen.')
    df.to_excel('transcripts_amazon.xlsx', index=False) # Speichern des DataFrame als Excel-Datei

bucket = 'BUCKET_NAME'

transcribe_all_files(bucket)