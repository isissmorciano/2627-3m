# Esercizio 06: Convertire un Voto in Giudizio

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Controllo di validità dei dati, intervalli semi-aperti con float)  
> **Obiettivo**: Separare i casi non validi prima di eseguire la classificazione dei dati.

## Obiettivo
Convertire un voto scolastico decimale in un giudizio sintetico, gestendo sia l'uscita con voto negativo sia l'errore per voti oltre il massimo.

## Regole di Valutazione
- Voto $< 0$: Stampa `"Uscita dal programma."`
- Voto $> 10$: Stampa `"Errore: voto fuori range."`
- Fasce valide:
  - Voto $< 5.0$: `"Giudizio: insufficiente"`
  - $5.0 \le$ Voto $\le 6.5$: `"Giudizio: sufficiente"`
  - $6.5 <$ Voto $\le 7.5$: `"Giudizio: buono"`
  - Voto $> 7.5$: `"Giudizio: ottimo"`

## Istruzioni
1. Chiedi all'utente un voto decimale: `voto: float = float(input(...))`.
2. Implementa la sequenza di verifiche nell'ordine corretto.
3. Stampa il messaggio o il giudizio corrispondente.

## Esempio di Esecuzione
```text
Inserisci un voto numerico (tra 0 e 10, o negativo per uscire): 7.0
Giudizio: buono
```
