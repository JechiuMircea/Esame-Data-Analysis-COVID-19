# Importazione delle librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Impostazioni di stile per i grafici
sns.set_style("whitegrid")  # Utilizziamo direttamente seaborn per lo stile
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# Lettura del dataset
print("Caricamento del dataset...")
df = pd.read_csv('data/owid-covid-data.csv')

# Conversione della colonna date in datetime
df['date'] = pd.to_datetime(df['date'])

# Filtro per Italia e anno 2022
italy_2022 = df[
    (df['location'] == 'Italy') & 
    (df['date'].dt.year == 2022)
].copy()

# Rimozione delle righe dove new_cases è nullo (giorni senza misurazioni)
italy_2022_clean = italy_2022.dropna(subset=['new_cases'])

print("\nAnalisi dati Italia 2022:")
print(f"Numero totale di giorni nel 2022: {len(italy_2022)}")
print(f"Numero di giorni con misurazioni: {len(italy_2022_clean)}")
print(f"Numero di giorni senza misurazioni: {len(italy_2022) - len(italy_2022_clean)}")

# 1. Grafico evoluzione casi totali
plt.figure(1)
plt.plot(italy_2022_clean['date'], italy_2022_clean['total_cases'], 
         linewidth=2, color='blue')
plt.title('Evoluzione Casi Totali COVID-19 in Italia (2022)')
plt.xlabel('Data')
plt.ylabel('Casi Totali')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output_grafici/4.3_italia_casi_totali.png')
plt.close()

# 2. Grafico nuovi casi
plt.figure(2)
plt.bar(italy_2022_clean['date'], italy_2022_clean['new_cases'],
        color='red', alpha=0.6)
plt.title('Nuovi Casi COVID-19 in Italia (2022)')
plt.xlabel('Data')
plt.ylabel('Nuovi Casi')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output_grafici/4.3_italia_nuovi_casi.png')
plt.close()

# Salvataggio statistiche in un file di testo
with open('output_grafici/4.3_italia_statistiche.txt', 'w', encoding='utf-8') as f:
    f.write("ANALISI COVID-19 ITALIA 2022\n")
    f.write("=" * 50 + "\n\n")
    
    f.write("STATISTICHE GENERALI\n")
    f.write("-" * 20 + "\n")
    f.write(f"Periodo analizzato: dal {italy_2022_clean['date'].min().strftime('%d/%m/%Y')} ")
    f.write(f"al {italy_2022_clean['date'].max().strftime('%d/%m/%Y')}\n")
    f.write(f"Totale giorni nel 2022: {len(italy_2022)}\n")
    f.write(f"Giorni con misurazioni: {len(italy_2022_clean)}\n")
    f.write(f"Giorni senza misurazioni: {len(italy_2022) - len(italy_2022_clean)}\n\n")
    
    f.write("STATISTICHE SUI CASI\n")
    f.write("-" * 20 + "\n")
    f.write(f"Casi totali inizio 2022: {int(italy_2022_clean['total_cases'].iloc[0]):,}\n")
    f.write(f"Casi totali fine 2022: {int(italy_2022_clean['total_cases'].iloc[-1]):,}\n")
    f.write(f"Nuovi casi nel 2022: {int(italy_2022_clean['new_cases'].sum()):,}\n")
    f.write(f"Media nuovi casi: {int(italy_2022_clean['new_cases'].mean()):,}\n")
    f.write(f"Massimo nuovi casi: {int(italy_2022_clean['new_cases'].max()):,}\n")

print("\nAnalisi completata!")
print("- Grafici salvati come '4.3_italia_casi_totali.png' e '4.3_italia_nuovi_casi.png'")
print("- Statistiche salvate in '4.3_italia_statistiche.txt'") 