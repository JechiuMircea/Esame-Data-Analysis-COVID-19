# Importazione delle librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Lettura del dataset
print("Caricamento del dataset...")
df = pd.read_csv('data/owid-covid-data.csv')

# Conversione della colonna date in datetime
df['date'] = pd.to_datetime(df['date'])

# Filtro per paesi e anno 2021
countries_data = df[
    (df['location'].isin(['Italy', 'Germany', 'France', 'Spain'])) &
    (df['date'].dt.year == 2021)
].copy()

# Analisi dei valori nulli
print("\nAnalisi valori nulli per paese:")
for country in ['Italy', 'Germany', 'France', 'Spain']:
    country_data = countries_data[countries_data['location'] == country]
    null_count = country_data['hosp_patients'].isna().sum()
    total_count = len(country_data)
    print(f"{country}: {null_count} valori nulli su {total_count} osservazioni")

# Calcolo statistiche per paese
stats = countries_data.groupby('location').agg({
    'hosp_patients': ['mean', 'max']  # Media e massimo
}).round(2)

# Rinomina le colonne per maggiore chiarezza
stats.columns = ['Media Giornaliera', 'Picco Massimo']

# Rimuoviamo la Germania dai grafici poiché non ha dati
stats = stats.dropna()

# Creazione del grafico a barre multiple
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Grafico della media giornaliera
ax1.bar(stats.index, stats['Media Giornaliera'], color=['red', 'green', 'orange'])
ax1.set_title('Media Giornaliera Pazienti Ospedalizzati COVID-19 (2021)')
ax1.set_ylabel('Numero Medio di Pazienti')
# Aggiunta delle etichette sopra le barre
for i, v in enumerate(stats['Media Giornaliera']):
    ax1.text(i, v, f'{int(v):,}', ha='center', va='bottom')

# Grafico del picco massimo
ax2.bar(stats.index, stats['Picco Massimo'], color=['darkred', 'darkgreen', 'darkorange'])
ax2.set_title('Picco Massimo Pazienti Ospedalizzati COVID-19 (2021)')
ax2.set_ylabel('Numero Massimo di Pazienti')
# Aggiunta delle etichette sopra le barre
for i, v in enumerate(stats['Picco Massimo']):
    ax2.text(i, v, f'{int(v):,}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('output_grafici/4.5_ospedalizzazioni.png')
plt.close()

# Salvataggio dei risultati
with open('output_grafici/4.5_statistiche_ospedali.txt', 'w', encoding='utf-8') as f:
    f.write("ANALISI OSPEDALIZZAZIONI COVID-19 (2021)\n")
    f.write("=" * 50 + "\n\n")
    
    f.write("STATISTICHE OSPEDALIZZAZIONI PER PAESE:\n")
    for country in ['Italy', 'Germany', 'France', 'Spain']:
        f.write(f"\n{country}:\n")
        if country in stats.index:
            f.write(f"- Media giornaliera: {int(stats.loc[country, 'Media Giornaliera']):,} pazienti\n")
            f.write(f"- Picco massimo: {int(stats.loc[country, 'Picco Massimo']):,} pazienti\n")
        else:
            f.write("- Dati non disponibili per il 2021\n")
    
    f.write("\nANALISI DATI MANCANTI:\n")
    f.write("La Germania non ha dati disponibili per le ospedalizzazioni nel 2021.\n")
    f.write("Per gli altri paesi, i dati sono completi e non presentano valori mancanti.\n")
    f.write("La sostituzione dei dati mancanti non è necessaria né consigliabile in questo caso.\n\n")
    
    f.write("NOTE:\n")
    f.write("- La media giornaliera rappresenta il numero medio di pazienti ospedalizzati in un giorno qualsiasi del 2021\n")
    f.write("- Il picco massimo rappresenta il numero più alto di pazienti ospedalizzati raggiunto nel 2021\n")
    f.write("- I calcoli considerano solo i paesi e i giorni con dati disponibili\n")

print("\nAnalisi completata!")
print("- Grafico salvato come '4.5_ospedalizzazioni.png'")
print("- Statistiche salvate in '4.5_statistiche_ospedali.txt'") 