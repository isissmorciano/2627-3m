# Esercizio 03: Lettura e Scrittura di Tabelle CSV

> **Prerequisiti teorici**: Modulo 03 (Cap. 07 - File CSV con `csv.DictReader` e `csv.DictWriter`)  
> **Obiettivo**: Manipolare file tabellari CSV convertendo automaticamente i tipi numerici.

## Obiettivo
Gestire l'import ed export di prodotti di magazzino in un file `prodotti.csv`.

## Il Contratto Software
1. `salva_prodotti_csv(prodotti: list[dict], percorso: str) -> None`:
   Usa `csv.DictWriter` (con `newline=""` ed intestazioni `fieldnames=["id", "nome", "prezzo", "quantita"]`) per scrivere i record su CSV.
2. `carica_prodotti_csv(percorso: str) -> list[dict]`:
   Usa `csv.DictReader` per leggere il CSV.  
   **Attenzione al Casting:** i dati letti da CSV sono tutti stringhe! La funzione deve convertire `"id"` e `"quantita"` in `int`, e `"prezzo"` in `float`. Se il file non esiste, restituisce `[]`.

## Formato del file `prodotti.csv`:
```csv
id,nome,prezzo,quantita
101,Tastiera,75.5,10
102,Mouse,25.0,20
```
