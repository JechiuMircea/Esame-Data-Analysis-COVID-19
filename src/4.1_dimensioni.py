# Importazione delle librerie necessarie
import pandas as pd

# Impostazioni di visualizzazione per pandas
pd.set_option('display.max_columns', None)  # Mostra tutte le colonne
pd.set_option('display.width', 1000)        # Larghezza output

# Lettura del dataset
print("Caricamento del dataset...")
df = pd.read_csv('data/owid-covid-data.csv')

# Conversione della colonna date in datetime
df['date'] = pd.to_datetime(df['date'])

# 1. ANALISI DIMENSIONI
print("\n1. DIMENSIONI DEL DATASET")
print("-" * 50)
print(f"Numero di righe: {df.shape[0]:,}")
print(f"Numero di colonne: {df.shape[1]:,}")
print(f"Periodo coperto: dal {df['date'].min()} al {df['date'].max()}")
print(f"Numero di paesi/regioni: {df['location'].nunique():,}")
if 'continent' in df.columns:
    print(f"Numero di continenti: {df['continent'].nunique():,}")

# 2. ANALISI METADATI
print("\n2. METADATI DELLE COLONNE")
print("-" * 50)
print("\nTipi di dati delle colonne:")
print(df.dtypes)

# Salvataggio dei risultati in un file di testo per riferimento futuro
with open('output_grafici/4.1_dataset_info.txt', 'w', encoding='utf-8') as f:
    f.write("ANALISI DIMENSIONI E METADATI DEL DATASET COVID-19\n")
    f.write("=" * 50 + "\n\n")
    
    f.write("1. DIMENSIONI\n")
    f.write("-" * 20 + "\n")
    f.write(f"Righe: {df.shape[0]:,}\n")
    f.write(f"Colonne: {df.shape[1]:,}\n")
    f.write(f"Periodo: {df['date'].min()} - {df['date'].max()}\n")
    f.write(f"Numero di paesi/regioni: {df['location'].nunique():,}\n")
    if 'continent' in df.columns:
        f.write(f"Numero di continenti: {df['continent'].nunique():,}\n\n")
    
    f.write("\n2. METADATI DELLE COLONNE\n")
    f.write("-" * 20 + "\n")
    f.write("Tipi di dati delle colonne:\n")
    f.write(df.dtypes.to_string())

print("\nAnalisi completata!")
print("- Le informazioni sono state salvate in 'output_grafici/4.1_dataset_info.txt'") 