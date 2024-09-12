import os
import azure.cognitiveservices.speech as speechsdk
import pandas as pd

def transcribe_all_files(file_path):
    # Konfigurieren der Sprachdienste mit dem Schlüssel und der Region
    speech_config = speechsdk.SpeechConfig(subscription='SCHLÜSSEL', region='STANDORT_REGION')
    
    speech_config.speech_recognition_language='de-DE' # Sprache auf Deutsch festlegen

    # Konfigurieren der Audiodatei für die Spracherkennung
    audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Durchführen der Spracherkennung
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    # Überprüfen, ob die Spracherkennung erfolgreich war
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print('file_name: {}'.format(os.path.basename(file_path)))
        print('transcript: {}'.format(speech_recognition_result.text) + '\n' + '='*100)
        # Speichern des Transkripts in einer Datenstruktur
        data = {'file_name': os.path.basename(file_path), 'transcript': speech_recognition_result.text}
    else:
        # Ausgabe, wenn keine Transkription erkannt wurde
        print('file_name: {}'.format(os.path.basename(file_path)))
        print('transcript:' + '\n' + '='*100)
        # Speichern einer leeren Transkription
        data = {'file_name': os.path.basename(file_path), 'transcript': ''}

    return data

# Pfad zum Ordner mit den Audiodateien
folder_path = 'ORDNERPFAD'

# Liste zur Speicherung der Transkripte
transcripts = []

# Durchlaufen aller Dateien im Ordner
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        # Transkribieren der Datei und Speichern des Ergebnisses in der Liste
        transcript = transcribe_all_files(file_path)
        transcripts.append(transcript)

# Konvertieren der Liste der Transkripte in ein DataFrame und Speichern als Excel-Datei
df = pd.DataFrame(transcripts)
df.to_excel('transcripts_microsoft.xlsx', index=False, engine='openpyxl')