# Progetto 01: Pipeline di Analisi Vendite da CSV

> **Prerequisiti teorici**: Modulo 03 (File CSV, Eccezioni, 3 Strati) e Modulo 05 (I 4 Pattern Fondamentali)  
> **Obiettivo**: Costruire una pipeline completa: apertura file $\to$ trasformazione dati $\to$ report finale.

## Lo Scenario
L'amministrazione di un piccolo e-commerce ti fornisce il file `ordini.csv`. Il programma deve caricare il file ed elaborare un report commerciale dettagliato per la direzione.

### Il File `ordini.csv`:
```csv
id_ordine,prodotto,categoria,quantita,prezzo_unitario
1,Laptop,Informatica,1,1200.0
2,Tastiera,Informatica,2,80.0
3,Manuale Python,Libri,5,35.0
4,Webcam,Informatica,1,50.0
5,Manuale SQL,Libri,3,30.0
```

## Architettura del Programma (Metodo Top-Down a 3 Strati)

1. **Strato I/O (Caricamento e Validazione)**

   - `carica_ordini(percorso_file: str) -> list[dict]`: apre il file CSV con `csv.DictReader`, effettua il casting dei numeri (`quantita: int`, `prezzo_unitario: float`) e restituisce la lista di dizionari. Se il file non esiste, intercetta `FileNotFoundError` e restituisce `[]`.

2. **Strato Logica Pura (I Pattern - Niente print!)**

   - `calcola_fatturato_totale(ordini: list[dict]) -> float`: (Aggregazione) somma `quantita * prezzo_unitario` di tutti gli ordini.
   - `conta_pezzi_per_categoria(ordini: list[dict], categoria: str) -> int`: (Filtraggio + Aggregazione) somma la quantità totale di articoli venduti per una specifica categoria.
   - `trova_ordine_top(ordini: list[dict]) -> dict | None`: (Ricerca) individua il record dell'ordine che ha generato il ricavo complessivo più alto.

3. **Strato Presentazione (La Voce)**

   - `stampa_report(fatturato: float, pezzi_libri: int, top_ordine: dict | None) -> None`: stampa una tabella pulita ed elegante.

4. **Orchestrazione (`main`)

Coordina i 3 strati in sequenza logica.
