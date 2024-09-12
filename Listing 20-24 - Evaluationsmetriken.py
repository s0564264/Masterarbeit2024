import pandas as pd
from sentence_transformers import SentenceTransformer, util
import jiwer

# Vorgefertigte SBERT-Modelle laden
model_name_similarity = 'all-MiniLM-L6-v2'
model_similarity = SentenceTransformer(model_name_similarity)

model_name_distance = 'all-MiniLM-L6-v2'
model_distance = SentenceTransformer(model_name_distance)

# Funktion zur Berechnung der Semantic Similarity
def calculate_similarity(sentence1, sentence2):
    if not sentence1 or not sentence2:
        return None
    embedding1 = model_similarity.encode(sentence1, convert_to_tensor=True) # Embedding des ersten Satzes
    embedding2 = model_similarity.encode(sentence2, convert_to_tensor=True) # Embedding des zweiten Satzes
    similarity = util.pytorch_cos_sim(embedding1, embedding2) # Kosinus-Ähnlichkeit berechnen
    return similarity.item()

# Funktion zur Berechnung der Semantic Distance
def calculate_distance(sentence1, sentence2):
    if not sentence1 or not sentence2:
        return None
    embedding1 = model_distance.encode(sentence1, convert_to_tensor=True) # Embedding des ersten Satzes
    embedding2 = model_distance.encode(sentence2, convert_to_tensor=True) # Embedding des zweiten Satzes
    similarity = util.pytorch_cos_sim(embedding1, embedding2) # Kosinus-Ähnlichkeit berechnen
    distance = 1 - similarity.item() # Semantic Distanz als 1 - Semantic Similarity berechnen
    return distance

# Funktion zur Berechnung der WER
def calculate_wer(reference, hypothesis):
    if not reference or not hypothesis:
        return None
    return jiwer.wer(reference, hypothesis) # WER zwischen Referenz und Hypothese berechnen

# Excel-Datei lesen
input_file = 'AUSGANGSDATEI.xlsx'  
df = pd.read_excel(input_file)
if 'sentence' not in df.columns or 'transcript' not in df.columns: # Sicherstellen, dass die erforderlichen Spalten existieren
    raise ValueError("Die Eingabe-Excel-Datei muss die Spalten 'sentence' und 'transcript' enthalten")

# Leere Zellen durch leere Zeichenketten ersetzen, damit die Funktionen richtig funktionieren
df['sentence'] = df['sentence'].fillna('')
df['transcript'] = df['transcript'].fillna('')

# WER, Semantic Similarity und Semantic Distance berechnen und neue Spalten in der Excel hinzufügen
df['WER'] = df.apply(lambda row: calculate_wer(row['sentence'], row['transcript']), axis=1)
df['Semantic Similarity'] = df.apply(lambda row: calculate_similarity(row['sentence'], row['transcript']), axis=1)
df['Semantic Distance'] = df.apply(lambda row: calculate_distance(row['sentence'], row['transcript']), axis=1)

# Ergebnisse in eine neue Excel-Datei speichern
output_file = 'AUSGABEDATEI.xlsx'  
df.to_excel(output_file, index=False, float_format="%.4f")

print(f"Ergebnisse wurden in {output_file} gespeichert")
