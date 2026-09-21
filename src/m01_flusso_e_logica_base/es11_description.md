# Esercizio 11: Somma di N Numeri con Ciclo for

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Il ciclo `for`, la funzione `range(n)`, il pattern accumulatore)  
> **Obiettivo**: Eseguire un blocco di codice un numero noto di volte e mantenere uno stato aggregato in memoria.

## Obiettivo
Chiedere all'utente quanti numeri desidera inserire, leggerli uno alla volta e calcolarne la somma complessiva.

## Istruzioni
1. Chiedi all'utente il numero totale di elementi da sommare: `n: int`.
2. Inizializza una variabile accumulatore: `somma: int = 0`.
3. Usa un ciclo `for i in range(n):` per leggere ciascun numero intero con messaggio personalizzato `"Inserisci il numero [i + 1]: "`.
4. Aggiungi ciascun valore a `somma`.
5. Al termine del ciclo, stampa: `"La somma totale è: [somma]"`.

## Esempio di Esecuzione
```text
Inserisci il numero di valori da sommare: 3
Inserisci il numero 1: 10
Inserisci il numero 2: 5
Inserisci il numero 3: 20
La somma totale è: 35
```
