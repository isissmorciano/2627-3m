# Esercizio 12: Somma dei Numeri in un Intervallo

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - `range(start, stop)` con due argomenti)  
> **Obiettivo**: Comprendere come generare sequenze numeriche consecutive con estremi personalizzati.

## Obiettivo
Calcolare la somma di tutti i numeri interi compresi tra due estremi inseriti dall'utente, inclusi gli estremi.

## Istruzioni
1. Chiedi l'estremo inferiore dell'intervallo: `estremo_inferiore: int`.
2. Chiedi l'estremo superiore dell'intervallo: `estremo_superiore: int` (assumere $\ge$ estremo inferiore).
3. Inizializza `somma: int = 0`.
4. Con un ciclo `for`, scorri tutti i numeri da `estremo_inferiore` fino a `estremo_superiore` (ricordando che in Python il secondo estremo di `range` è escluso, quindi occorre indicare `estremo_superiore + 1`).
5. Stampa:  
   `"La somma dei numeri nell'intervallo [[estremo_inferiore], [estremo_superiore]] è: [somma]"`

## Esempio di Esecuzione
```text
Inserisci l'estremo inferiore dell'intervallo: 5
Inserisci l'estremo superiore dell'intervallo: 9
La somma dei numeri nell'intervallo [5, 9] è: 35
```
