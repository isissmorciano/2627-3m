# Esercizio 05: Sigla Mese e Stagione

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Metodi di stringa `.strip()`, `.upper()`, operatore `in` con liste)  
> **Obiettivo**: Normalizzare una stringa in ingresso e verificare l'appartenenza a un gruppo di valori ammessi.

## Obiettivo
Data la sigla di tre lettere di un mese, verificare se è valida e stampare a quale stagione appartiene.

## Mappatura Stagioni
- **Inverno**: DIC, GEN, FEB
- **Primavera**: MAR, APR, MAG
- **Estate**: GIU, LUG, AGO
- **Autunno**: SET, OTT, NOV

## Istruzioni
1. Chiedi all'utente la sigla del mese e normalizzala: usa `.strip()` per rimuovere spazi e `.upper()` per convertirla in maiuscolo.
2. Controlla a quale stagione appartiene usando l'operatore `in` su liste di stringhe.
3. Se la sigla non corrisponde a nessun mese valido, stampa `"Sigla mese inesistente."` e termina.
4. Se valida, stampa: `"Il mese [mese] appartiene alla stagione: [stagione]."`

## Esempio di Esecuzione
```text
Inserisci la sigla del mese (es. GEN): apr
Il mese APR appartiene alla stagione: primavera.
```
