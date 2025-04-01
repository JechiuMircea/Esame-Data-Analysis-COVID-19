# Esame Data Analysis COVID-19

## Esecuzione degli Script
Ogni script può essere eseguito indipendentemente:

```bash
python src/4.1_dimensioni.py  # Analisi dimensioni e metadati
python src/4.2_continenti.py  # Analisi per continente
python src/4.3_italia.py      # Focus Italia 2022
python src/4.4_intensive.py   # Analisi terapie intensive
python src/4.5_ospedali.py    # Analisi ospedalizzazioni
```

## Descrizione delle Analisi e Risultati

### 4.1 Dimensioni e Metadati
- Analisi delle dimensioni del dataset
- Esplorazione dei metadati
- Verifica della qualità dei dati

#### Risultati 4.1
![Distribuzione dei dati mancanti](output_grafici/4.1_missing_data.png)
- Dimensioni del dataset: X righe × Y colonne
- Principali statistiche: [verranno aggiunte]

### 4.2 Analisi per Continente
- Calcolo dei casi totali per continente
- Analisi delle percentuali sul totale mondiale
- Visualizzazioni comparative

#### Risultati 4.2
![Casi totali per continente](output_grafici/4.2_total_cases_continent.png)
![Percentuali sul totale mondiale](output_grafici/4.2_percentages_continent.png)
- Tabella riassuntiva: [verrà aggiunta]

### 4.3 Focus Italia 2022
- Analisi dell'evoluzione dei casi totali
- Studio dei nuovi casi
- Gestione dei dati mancanti

#### Risultati 4.3
![Evoluzione casi totali Italia 2022](output_grafici/4.3_italy_total_cases.png)
![Nuovi casi Italia 2022](output_grafici/4.3_italy_new_cases.png)
- Trend principali: [verranno aggiunti]

### 4.4 Confronto Terapie Intensive
- Confronto tra Italia, Germania e Francia
- Analisi del periodo maggio 2022 - aprile 2023
- Visualizzazioni statistiche

#### Risultati 4.4
![Boxplot terapie intensive](output_grafici/4.4_icu_boxplot.png)
- Analisi comparativa: [verrà aggiunta]

### 4.5 Analisi Ospedalizzazioni
- Studio dei dati di Italia, Germania, Francia e Spagna
- Analisi dei dati mancanti
- Valutazione delle possibilità di sostituzione

#### Risultati 4.5
![Ospedalizzazioni per paese](output_grafici/4.5_hospitalizations.png)
- Analisi dei dati mancanti: [verrà aggiunta]

## Note Importanti
- Tutti i grafici vengono salvati nella cartella `output_grafici/` e sono visualizzabili direttamente su GitHub
- Ogni script include commenti dettagliati per ogni riga di codice
- I risultati delle analisi vengono documentati sia nel codice che in questo README

## Autore
Mircea Jechiu

## Licenza
Questo progetto è distribuito sotto licenza MIT. 