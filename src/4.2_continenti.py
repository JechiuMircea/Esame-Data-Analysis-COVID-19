# Importazione delle librerie necessarie
import pandas as pd

# Lettura del dataset
print("Caricamento del dataset...")
df = pd.read_csv('data/owid-covid-data.csv')

# Conversione della colonna date in datetime
df['date'] = pd.to_datetime(df['date'])

# Filtriamo solo le righe relative ai continenti
continents_data = df[df['location'].isin(['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania'])]

# Prendiamo l'ultima riga disponibile per ogni continente (dati più recenti)
latest_data = continents_data.groupby('location').last().reset_index()

# Calcoliamo il totale mondiale dei casi
total_world_cases = latest_data['total_cases'].sum()

# Creiamo un DataFrame con i risultati
results = pd.DataFrame({
    'Continente': latest_data['location'],
    'Casi Totali': latest_data['total_cases'],
    'Percentuale sul Totale': (latest_data['total_cases'] / total_world_cases * 100)
})

# Ordiniamo i risultati per numero di casi (decrescente)
results = results.sort_values('Casi Totali', ascending=False)

# Formattazione dei numeri
results['Casi Totali'] = results['Casi Totali'].apply(lambda x: f"{int(x):,}")
results['Percentuale sul Totale'] = results['Percentuale sul Totale'].apply(lambda x: f"{x:.2f}%")

# Stampa dei risultati
print("\nANALISI CASI COVID-19 PER CONTINENTE")
print("-" * 50)
print("\nRisultati dell'analisi:")
print(results.to_string(index=False))
print("\nNota: i dati si riferiscono all'ultima data disponibile nel dataset")

# Salvataggio dei risultati in un file di testo
with open('output_grafici/4.2_risultati_continenti.txt', 'w', encoding='utf-8') as f:
    f.write("ANALISI CASI COVID-19 PER CONTINENTE\n")
    f.write("=" * 50 + "\n\n")
    f.write("Dati riferiti all'ultima data disponibile nel dataset\n\n")
    f.write(results.to_string(index=False))
    f.write(f"\n\nTotale mondiale: {int(total_world_cases):,} casi") 