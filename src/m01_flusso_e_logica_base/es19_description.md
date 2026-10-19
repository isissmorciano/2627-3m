# Esercizio 19: Riepilogo degli interi inseriti con il ciclo while

> **Prerequisiti teorici**: Modulo 01 (ciclo `while`, valore sentinella, condizioni, contatori e accumulatore)
> **Obiettivo**: Elaborare una sequenza di lunghezza non nota e mantenere più valori di riepilogo.

## Obiettivo
Leggere interi fino a quando viene inserito 0. Al termine, mostrare quanti valori positivi e quanti negativi sono stati inseriti, oltre alla loro somma. Lo 0 termina l'inserimento e non è conteggiato né sommato.

## Istruzioni
1. Inizializza a 0 i contatori dei positivi e dei negativi e la variabile `somma`.
2. Leggi un numero intero.
3. Finché il numero è diverso da 0:
   - Se è positivo, incrementa il contatore dei positivi.
   - Altrimenti, incrementa il contatore dei negativi.
   - Aggiungi il numero a `somma`.
   - Leggi il numero successivo.
4. Stampa il numero dei positivi, il numero dei negativi e la somma, ciascuno su una riga.

## Esempio di Esecuzione
```text
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): -2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 0
Numeri positivi: 2
Numeri negativi: 1
Somma: 9
```
