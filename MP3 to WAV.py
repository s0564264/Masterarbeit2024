import os
from pydub import AudioSegment

source_folder_path = "PFAD_QUELLORDNER"
destination_folder_path = "PFAD_ZIELORDNER"

# Zielverzeichnis erstellen, falls es noch nicht existiert
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

# Liste aller Dateien im Quellverzeichnis abrufen
files = os.listdir(source_folder_path)

# Jede Datei im Verzeichnis durchlaufen
for file in files:
    src = os.path.join(source_folder_path, file) # Den vollständigen Pfad zur Datei abrufen
    
    # Überprüfen, ob es sich um eine .mp3-Datei handelt
    if src.endswith(".mp3"):
        sound = AudioSegment.from_mp3(src) # .mp3-Datei in .wav-Datei konvertieren
        file_name = os.path.splitext(file)[0] # Dateiname ohne Erweiterung abrufen
        destination = os.path.join(destination_folder_path, file_name + ".wav") # Den vollständigen Pfad zur Zieldatei abrufen
        sound.export(destination, format="wav") # Die konvertierte Audiodatei exportieren