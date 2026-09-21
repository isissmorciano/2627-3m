# Esercizio 02: Saluto Interattivo e Calcolo dell'Età

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Costanti, Input testuale vs numerico, Operazioni aritmetiche)  
> **Obiettivo**: Usare una costante per ricavare un dato calcolato a partire dall'anno di nascita.

## Obiettivo
Calcolare l'età approssimativa di un utente a partire dal suo anno di nascita e visualizzare un messaggio personalizzato.

## Istruzioni
1. Definisci a inizio file la costante `ANNO_CORRENTE: int = 2026`.
2. Chiedi all'utente il suo nome e assegnalo alla variabile `nome_utente: str`.
3. Chiedi all'utente il suo anno di nascita, convertilo in intero con `int()` e assegnalo a `anno_nascita: int`.
4. Calcola l'età approssimativa sottraendo l'anno di nascita dall'`ANNO_CORRENTE`.
5. Stampa a video:  
   `"Ciao [nome_utente]! Quest'anno compi circa [eta_utente] anni."`

## Esempio di Esecuzione
```text
Inserisci il tuo nome: Anna
Inserisci il tuo anno di nascita: 1990
Ciao Anna! Quest'anno compi circa 36 anni.
```
