import pandas as pd

input_file = 'AUSGANGSDATEI.xlsx'
output_file = 'AUSGANGSDATEI.xlsx'

df = pd.read_excel(input_file) # Einlesen der Excel-Datei in ein DataFrame

properties = ['age', 'gender', 'accents'] # Definition der Spracheigenschaften

unique_combinations = df.drop_duplicates(subset=properties)[properties] # Entfernt Duplikate basierend auf den Werten in den angegebenen Spalten und behält nur die eindeutigen Kombinationen dieser Spalten

stratified_sample = pd.DataFrame() # Initialisierung eines leeren DataFrames für die geschichtete Stichprobe

# Iteration über jede einzigartige Kombination
for _, combo in unique_combinations.iterrows():
    # Filterung des DataFrames für die aktuelle Kombination
    subset = df[(df['age'] == combo['age']) & 
                (df['gender'] == combo['gender']) & 
                (df['accents'] == combo['accents'])]
    
    if not subset.empty:
        # Wenn mindestens 20 Datensätze vorhanden sind, ziehe 20 ohne Ersetzung
        if len(subset) >= 20:
            sampled_subset = subset.sample(n=20, replace=False)
        # Wenn weniger als 20 Datensätze vorhanden sind, dupliziere bis 20 erreicht sind
        else:
            # Anzahl der zusätzlich benötigten Datensätze
            additional_needed = 20 - len(subset)
            sampled_subset = subset.copy()
            # Wenn zusätzliche Datensätze benötigt werden, dupliziere vorhandene Datensätze
            if additional_needed > 0:
                duplicates = subset.sample(n=additional_needed, replace=True)
                sampled_subset = pd.concat([sampled_subset, duplicates])
        stratified_sample = pd.concat([stratified_sample, sampled_subset]) # Hinzufügen zur geschichteten Stichprobe

stratified_sample.reset_index(drop=True, inplace=True) # Zurücksetzen des Index des finalen DataFrames

stratified_sample.to_excel(output_file, index=False)