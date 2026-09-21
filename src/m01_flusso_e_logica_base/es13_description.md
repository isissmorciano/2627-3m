# Esercizio 13: Validazione di un Input Positivo con while

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Il ciclo indefinito `while True`, l'istruzione `break`)  
> **Obiettivo**: Ripetere l'acquisizione finché l'utente non fornisce un valore conforme ai vincoli del programma.

## Obiettivo
Chiedere ripetutamente all'utente un numero intero positivo, mostrando un messaggio di errore a ogni inserimento non valido, e terminare solo quando viene fornito un valore strettamente maggiore di zero.

## Istruzioni
1. Avvia un ciclo indefinito `while True:`.
2. Leggi un numero intero dall'utente: `numero: int = int(input("Inserisci un numero positivo: "))`.
3. Controlla il valore:
   - Se `numero > 0`: stampa `"Numero valido: [numero]"` ed esci immediatamente dal ciclo con `break`.
   - Se `numero <= 0`: stampa `"Errore: il numero deve essere positivo."` e lascia che il ciclo riparta.

## Esempio di Esecuzione
```text
Inserisci un numero positivo: -5
Errore: il numero deve essere positivo.
Inserisci un numero positivo: 0
Errore: il numero deve essere positivo.
Inserisci un numero positivo: 12
Numero valido: 12
```
