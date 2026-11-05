# Esercizio 21: Spedizione Gratuita

> **Prerequisiti teorici**: Modulo 01 (confronti numerici, `and`, `or`, `not`, parentesi e `if / else`)
> **Obiettivo**: Tradurre una regola commerciale con soglie e condizioni aggiuntive in un'espressione booleana.

## Obiettivo
Calcolare se un ordine ha diritto alla spedizione gratuita. La spedizione è gratuita per ordini di almeno 50 euro, oppure per ordini di almeno 30 euro effettuati da un membro del club. Per le zone remote, la soglia è sempre di 80 euro.

## Istruzioni
1. Chiedi il totale dell'ordine e convertilo in `float`.
2. Chiedi se il cliente è membro del club e se abita in una zona remota. Usa `s` per sì e `n` per no e ricava due variabili booleane.
3. Calcola `spedizione_gratuita` con un'espressione booleana che rispetti entrambe le regole:
   - la soglia ordinaria è raggiunta con almeno 50 euro, oppure con almeno 30 euro se il cliente è membro;
   - in una zona remota, il totale deve comunque essere almeno 80 euro.
4. Stampa `"Spedizione gratuita."` oppure `"Spedizione a pagamento."`.
5. Prova gli importi esatti delle soglie (30, 50 e 80 euro) e importi appena inferiori.

## Esempio di Esecuzione
```text
Totale dell'ordine in euro: 35
Sei membro del club? (s/n): s
Abiti in una zona remota? (s/n): n
Spedizione gratuita.
```
