import pandas as pd

source_file_path = 'validated.xlsx'
destination_file_path = 'transcripts_amazon.xlsx'

# Einlesen der Excel-Dateien
df_original = pd.read_excel(source_file_path)
df_transcribed = pd.read_excel(destination_file_path)

# Sicherstellen, dass 'file_name' eine Spalte in beiden DataFrames ist
if 'file_name' not in df_original.columns:
    raise ValueError("Spalte 'file_name' nicht in df_original gefunden.")
if 'file_name' not in df_transcribed.columns:
    raise ValueError("Spalte 'file_name' nicht in df_transcribed gefunden.")

# Umbenennen von 'file_name' in df_transcribed, um es zu unterscheiden
df_transcribed = df_transcribed.rename(columns={'file_name': 'file_name_transcribed'})

# Zusammenführen der DataFrames auf Basis von 'file_name'
combined_df = pd.merge(df_original, df_transcribed, left_on='file_name', right_on='file_name_transcribed')

# Speichern des kombinierten DataFrames in einer neuen Excel-Datei
output_path = 'combined_file_amazon.xlsx'
combined_df.to_excel(output_path, index=False)

print(f"Die kombinierte Datei wurde unter {output_path} gespeichert")
