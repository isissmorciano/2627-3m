# Esercizio 22: Requisiti per una Borsa di Studio

> **Prerequisiti teorici**: Modulo 01 (confronti, condizioni booleane composte, `and`, `or`, `not` e `if / else`)
> **Obiettivo**: Verificare più requisiti, includendo alternative e soglie inclusive.

## Obiettivo
Stabilire se uno studente può ottenere una borsa di studio. Deve essere residente nella regione, non avere sanzioni disciplinari e avere una media di almeno 8. Inoltre, deve rispettare una delle due condizioni economiche:
- reddito familiare non superiore a 20.000 euro;
- media di almeno 9 e reddito familiare non superiore a 30.000 euro.

## Istruzioni
1. Chiedi la media scolastica come numero decimale e il reddito familiare in euro come numero intero.
2. Chiedi se lo studente è residente nella regione e se ha sanzioni disciplinari. Usa `s` per sì e `n` per no e ricava due variabili booleane.
3. Calcola `idoneo` combinando tutti i requisiti. Usa le parentesi per evidenziare le due alternative relative al reddito.
4. Stampa `"Studente idoneo."` oppure `"Studente non idoneo."`.
5. Verifica i limiti esatti di media e reddito, oltre a casi in cui manca un requisito non economico.

## Esempio di Esecuzione
```text
Inserisci la media scolastica: 9
Inserisci il reddito familiare: 28000
Sei residente nella regione? (s/n): s
Hai sanzioni disciplinari? (s/n): n
Studente idoneo.
```
