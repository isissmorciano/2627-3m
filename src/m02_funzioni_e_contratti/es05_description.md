# Esercizio 05: Calcolatrice Modulare

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Procedure di menu, funzioni con valore di ritorno `float | None`)  
> **Obiettivo**: Scomporre un programma interattivo in funzioni specializzate a compito singolo.

## Obiettivo
Realizzare una calcolatrice a 4 operazioni suddivisa in funzioni dedicate.

## Struttura delle Funzioni Richieste
1. `chiedi_numeri() -> tuple[float, float]`: Chiede all'utente due numeri e li restituisce.
2. `scegli_operazione() -> str`: Mostra il menu e restituisce il simbolo dell'operazione scelta (`"+"`, `"-"`, `"*"`, `"/"`). Se non valida, restituisce stringa vuota `""`.
3. `calcola(num1: float, num2: float, operazione: str) -> float | None`: Esegue il calcolo. Gestisce la divisione per zero restituendo `None`.
4. `main() -> None`: Funzione di orchestrazione che collega le parti.

## Esempio di Esecuzione
```text
Benvenuto nella Calcolatrice Modulare!
Inserisci il primo numero: 10
Inserisci il secondo numero: 2
Scegli un'operazione (+, -, *, /): /
Il risultato è: 5.0
```
