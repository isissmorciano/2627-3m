# Esercizio 03: Saluto e Fascia d'Età

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - La selezione: `if / elif / else` a cascata)  
> **Obiettivo**: Classificare un valore numerico in intervalli disgiunti ed eseguire rami di codice diversi.

## Obiettivo
Acquisire nome ed età dell'utente, stampare un saluto e determinare la sua fascia anagrafica.

## Istruzioni
1. Chiedi il nome all'utente (`nome: str`).
2. Chiedi l'età all'utente e convertila in intero (`eta: int`).
3. Stampa il saluto: `"Ciao [nome]!"`.
4. Mediante una catena `if / elif / else`, stampa la classificazione:
   - Se `eta < 18`: stampa `"Sei minorenne."`
   - Altrimenti se `eta < 65`: stampa `"Sei adulto."`
   - Altrimenti: stampa `"Sei anziano."`

## Esempio di Esecuzione
```text
Inserisci il tuo nome: Mario
Inserisci la tua età: 25
Ciao Mario!
Sei adulto.
```
