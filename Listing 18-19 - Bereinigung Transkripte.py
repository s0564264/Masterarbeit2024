import pandas as pd
import re

# Funktion definieren, um Satzzeichen zu entfernen und den Text in Kleinbuchstaben umzuwandeln
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

# Excel-Datei laden
combined_file_path = 'combined_file_commonvoice.xlsx'  
df = pd.read_excel(combined_file_path)

# Die Spalten 'sentence' und 'transcript' bereinigen
df['sentence'] = df['sentence'].apply(lambda x: clean_text(str(x)))
df['transcript'] = df['transcript'].apply(lambda x: clean_text(str(x)))

# Den modifizierten DataFrame in eine neue Excel-Datei speichern
output_file_path = 'cleaned_file_commonvoice.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Bereinigte und in Kleinbuchstaben konvertierte Daten wurden in {output_file_path} gespeichert")
