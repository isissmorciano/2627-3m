# Esercizio 04: Sanzioni Codice della Strada

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Confronti numerici con `<=`, catena `if / elif / else`)  
> **Obiettivo**: Calcolare una tariffa a scaglioni in base a una grandezza numerica.

## Obiettivo
Dato l'eccesso di velocità in km/h registrato da un tachimetro, calcolare l'importo della sanzione amministrativa.

## Tabella delle Sanzioni
- Fino a 10 km/h (compresi): 36 €
- Da oltre 10 km/h fino a 40 km/h (compresi): 148 €
- Da oltre 40 km/h fino a 60 km/h (compresi): 370 €
- Oltre 60 km/h: 500 €

## Istruzioni
1. Chiedi all'utente l'eccesso di velocità come numero intero: `eccesso: int`.
2. Applica la catena di condizioni per determinare la variabile `multa: int`.
3. Stampa il risultato nel formato:  
   `"La sanzione amministrativa è di euro [multa]."`

## Esempio di Esecuzione
```text
Inserisci l'eccesso di velocità in km/h: 25
La sanzione amministrativa è di euro 148.
```
