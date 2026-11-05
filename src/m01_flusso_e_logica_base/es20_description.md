# Esercizio 20: Accesso al Laboratorio

> **Prerequisiti teorici**: Modulo 01 (operatori di confronto, `and`, `or`, `not` e parentesi)
> **Obiettivo**: Combinare più condizioni booleane per decidere se autorizzare un accesso.

## Obiettivo
Stabilire se una persona può usare il laboratorio della scuola. Per entrare deve avere una tessera attiva e non sospesa. Inoltre, deve aver completato il corso di sicurezza oppure avere almeno 16 anni e un'autorizzazione.

## Istruzioni
1. Chiedi l'età e convertila in intero.
2. Chiedi se la persona ha una tessera, ha completato il corso, ha un'autorizzazione e ha la tessera sospesa. Per ogni risposta, usa `s` per sì e `n` per no, e ricava una variabile booleana.
3. Costruisci l'espressione `puo_usare_il_laboratorio` applicando tutte le regole:
   - la persona ha la tessera;
   - la tessera non è sospesa;
   - ha completato il corso **oppure** ha almeno 16 anni **e** ha un'autorizzazione.
4. Stampa `"Accesso consentito."` se la condizione è vera, altrimenti `"Accesso negato."`.
5. Verifica anche casi in cui una sola delle condizioni richieste non è rispettata.

## Esempio di Esecuzione
```text
Inserisci la tua età: 16
Hai una tessera? (s/n): s
Hai completato il corso di sicurezza? (s/n): n
Hai un'autorizzazione? (s/n): s
La tessera è sospesa? (s/n): n
Accesso consentito.
```
