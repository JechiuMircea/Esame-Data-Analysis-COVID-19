# Analisi Dati COVID-19

## Descrizione del Progetto
Questo progetto analizza i dati della pandemia COVID-19 utilizzando il dataset di Our World in Data. L'analisi è strutturata in cinque parti principali, ognuna focalizzata su aspetti specifici dei dati.

## Struttura del Repository
```
.
├── src/                    # Script Python per le analisi
├── output_grafici/         # Grafici e file di statistiche generati
├── docs/                   # Documentazione aggiuntiva
└── requirements.txt        # Dipendenze Python necessarie
```

## Prerequisiti
- Python 3.8 o superiore
- Librerie Python: pandas, matplotlib, seaborn
- Dataset: owid-covid-data.csv (da scaricare separatamente)

## Installazione
```bash
# Creazione ambiente virtuale
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Installazione dipendenze
pip install -r requirements.txt
```

## Analisi e Risultati

### 4.1 Dimensioni e Metadati
- **Obiettivo**: Analisi della struttura e qualità del dataset
- **Risultati**:
  - Dataset contiene dati globali sulla pandemia
  - Struttura: dati giornalieri per paese/regione
  - Metriche principali: casi, decessi, ospedalizzazioni, vaccinazioni

### 4.2 Analisi per Continente
- **Obiettivo**: Studio della distribuzione dei casi per continente
- **Risultati**:
  - Analisi della distribuzione geografica dei casi
  - Calcolo delle percentuali sul totale mondiale
  - Visualizzazione comparativa tra continenti

### 4.3 Focus Italia 2022
- **Obiettivo**: Analisi dettagliata dei casi in Italia nel 2022
- **Risultati**:
  - Evoluzione temporale dei casi totali
  - Andamento dei nuovi casi giornalieri
  - Identificazione dei periodi di maggiore incidenza

### 4.4 Confronto Terapie Intensive
- **Obiettivo**: Confronto tra Italia, Germania e Francia (mag 2022 - apr 2023)
- **Risultati**:
  - Analisi tramite boxplot delle distribuzioni
  - L'Italia ha mostrato il minor numero di pazienti in terapia intensiva
  - Differenza di circa il 50% rispetto agli altri paesi analizzati

### 4.5 Analisi Ospedalizzazioni 2021
- **Obiettivo**: Studio comparativo delle ospedalizzazioni
- **Risultati**:
  - Analisi di Italia, Francia e Spagna (Germania: dati non disponibili)
  - Confronto delle medie giornaliere e dei picchi massimi
  - Valutazione dell'impatto sui sistemi ospedalieri

## Esecuzione degli Script
Ogni script può essere eseguito indipendentemente:
```bash
python src/4.1_dimensioni.py
python src/4.2_continenti.py
python src/4.3_italia.py
python src/4.4_confronto_ti.py
python src/4.5_ospedali.py
```

## Note Tecniche
- Gli script gestiscono automaticamente i dati mancanti
- I risultati vengono salvati sia come grafici che come file di testo
- Ogni analisi include verifiche sulla qualità dei dati

## Autore
Mircea Jechiu

## Licenza
MIT License 