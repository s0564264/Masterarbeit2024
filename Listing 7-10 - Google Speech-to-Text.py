import os
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import pandas as pd

def transcribe_all_files(
    project_id: str,
    folder_path: str,
) -> None:
    transcripts_df = pd.DataFrame(columns=['file_name', 'transcript']) # Initialisieren des DataFrames zur Speicherung aller Transkripte
    client = SpeechClient.from_service_account_json('key.json') # Erstellen des SpeechClient unter Verwendung der Service Account JSON-Datei

    # Durchlaufen aller Dateien im angegebenen Ordner
    for file_name in os.listdir(folder_path):
        # Überprüfen, ob die Datei eine MP3-Datei ist
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)

            # Lesen der MP3-Datei
            with open(file_path, 'rb') as f:
                mp3_data = f.read()

            # Konfiguration für die Spracherkennung
            config = cloud_speech.RecognitionConfig(
                auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
                language_codes=["de-DE"],
                model='latest_short',
                features = cloud_speech.RecognitionFeatures(
                    enable_automatic_punctuation=True
                ) 
            )

            # Erstellen der Anfrage für die Spracherkennung
            request = cloud_speech.RecognizeRequest(
                recognizer=f"projects/{project_id}/locations/global/recognizers/_",
                config=config,
                content=mp3_data
            )
            
            response = client.recognize(request=request) # Senden der Anfrage und Empfangen der Antwort

            # Ausgabe des Dateinamens und des Transkripts
            print(f'file_name: {file_name}')
            transcript = ''
            for result in response.results:
                transcript += result.alternatives[0].transcript
            print('transcript: ' + transcript + '\n' + '='*100)
            
            current_transcript_df = pd.DataFrame([{'file_name': file_name, 'transcript': transcript}]) # Erstellen eines neuen DataFrame für die aktuelle Datei
            transcripts_df = pd.concat([transcripts_df, current_transcript_df], ignore_index=True) # Anhängen des neuen DataFrame an den Haupt-DataFrame
    transcripts_df.to_excel('transcripts_google.xlsx', index=False) # Speichern des DataFrames als Excel-Datei

# Aufrufen der Funktion zur Transkription aller Dateien im Ordner
transcribe_all_files(project_id="PROJEKT_ID", folder_path="ORDNERPFAD")