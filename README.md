# Test der Erkennungsgüte von Spracherkennungssoftwares in Abhängigkeit von Spracheigenschaften mithilfe des Common Voice Datensatzes
| Matrikelnummer: 564264 | Name, Vorname: Luu, Carmen | HTW Berlin | 2024 |
|-|-|-|-|

Dieses Repository enthält alle Code-Dateien die für diese Masterarbeit verwendet wurden.

## Dateien im Repository
| Dateiname                          | Beschreibung                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| MP3 to WAV.py                       | Konvertiert MP3-Dateien in das WAV-Format zur Kompatibilität mit bestimmten ASR-Systemen.|
| Listing 1 - Geschichtete Stichprobe.py | Skript zur Ziehung einer geschichteten Stichprobe.|
| Listing 2 - Extraktion MP3-Dateien.py | Extrahiert MP3-Dateien zur weiteren Verarbeitung.|
| Listing 3-6 - Amazon Transcribe.py  | Implementiert die Transkription mittels Amazon Transcribe.|
| Listing 7-10 - Google Speech-to-Text.py | Implementiert die Transkription mittels Google Speech-to-Text.|
| Listing 11-14 - Microsoft Speech-to-Text.py | Implementiert die Transkription mittels Microsoft Speech-to-Text.|
| Listing 15-17 - Zusammenführung Excel-Dateien.py | Fügt die verschiedenen Transkriptionsergebnisse in einer Excel-Datei zusammen.|
| Listing 18-19 - Bereinigung Transkripte.py | Bereinigt die erzeugten Transkripte zur weiteren Analyse.|
| Listing 20-24 - Evaluationsmetriken.py | Berechnet die Metriken zur Bewertung der Erkennungsgüte.|
| Boxplots und Excels - Common Voice.R| Erzeugt Boxplots und Excel-Auswertungen basierend auf den Daten aus dem Common Voice Datensatz.|
| Boxplots und Excels - eigener Datensatz.R | Generiert Boxplots und Excel-Auswertungen für den eigenen Datensatz.|

Stand: 12.09.2024
