# Esercizio 08: Verifica Anno Bisestile

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Operatore modulo `%`, connettivi booleani `and` e `or`, parentesi logiche)  
> **Obiettivo**: Tradurre un algoritmo di calendario con logica combinata in un'espressione booleana pulita.

## Obiettivo
Verificare se un anno intero inserito dall'utente è bisestile secondo il calendario gregoriano.

## Regola del Calendario Gregoriano
Un anno è bisestile se:
- È divisibile per 4 **E** non è divisibile per 100,
- **OPPURE** se è divisibile per 400.

*(Ad esempio: il 2024 e il 2000 sono bisestili, mentre il 2023 e il 1900 non lo sono).*

## Istruzioni
1. Chiedi all'utente di inserire un anno come numero intero: `anno: int`.
2. Verifica la condizione con l'operatore modulo `%`:
   - `anno % 4 == 0`
   - `anno % 100 != 0`
   - `anno % 400 == 0`
3. Stampa:
   - `"L'anno [anno] è bisestile."` oppure
   - `"L'anno [anno] non è bisestile."`

## Esempio di Esecuzione
```text
Inserisci un anno: 2024
L'anno 2024 è bisestile.
```
