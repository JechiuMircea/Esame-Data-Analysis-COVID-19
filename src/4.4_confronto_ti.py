# Importazione delle librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Impostazioni di stile per i grafici
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# Lettura del dataset
print("Caricamento del dataset...")
df = pd.read_csv('data/owid-covid-data.csv')

# Conversione della colonna date in datetime
df['date'] = pd.to_datetime(df['date'])

# Verifica valori nulli nella colonna icu_patients
print("\nAnalisi valori mancanti:")
missing_icu = df[df['icu_patients'].isna()]
print(f"Righe con valori mancanti in icu_patients: {len(missing_icu)}")

# Filtro per paesi e periodo di interesse
countries_data = df[
    (df['location'].isin(['Italy', 'Germany', 'France'])) &
    (df['date'] >= '2022-05-01') &
    (df['date'] <= '2023-04-30')
].copy()

# Verifica dati disponibili per paese
print("\nNumero di osservazioni per paese:")
print(countries_data.groupby('location').size())

# Creazione del boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=countries_data, x='location', y='icu_patients')
plt.title('Confronto Pazienti in Terapia Intensiva\n(Maggio 2022 - Aprile 2023)')
plt.xlabel('Paese')
plt.ylabel('Numero di Pazienti in TI')

# Salvataggio del grafico
plt.tight_layout()
plt.savefig('output_grafici/4.4_confronto_ti_boxplot.png')
plt.close()

# Calcolo statistiche descrittive
stats = countries_data.groupby('location')['icu_patients'].describe()
print("\nStatistiche descrittive per paese:")
print(stats)

# Salvataggio statistiche in un file di testo
with open('output_grafici/4.4_statistiche_ti.txt', 'w', encoding='utf-8') as f:
    f.write("ANALISI COMPARATIVA TERAPIE INTENSIVE\n\n")
    f.write("Dall'analisi effettuata ho notato che l'Italia è stato il paese con minor numero di pazienti\n in terapia intensiva rispetto ai paesi con i quali abbiamo fatto il confronto, con almeno il 50% di pazienti in meno all'incirca.")
    
    f.write("\n\nNOTE:\n")
    f.write("- Il boxplot mostra la distribuzione dei pazienti in terapia intensiva\n")
    f.write("- I box rappresentano il 25°, 50° (mediana) e 75° percentile\n")
    f.write("- I whiskers mostrano i valori min/max (esclusi outlier)\n")
    f.write("- I punti rappresentano gli outlier\n")

print("\nAnalisi completata!")
print("- Grafico salvato come '4.4_confronto_ti_boxplot.png'")
print("- Statistiche salvate in '4.4_statistiche_ti.txt'") 