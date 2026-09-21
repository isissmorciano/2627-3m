# Esercizio 02: Calcolo Sconto con Validazione dei Parametri

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Regole del Contratto, gestione input non validi con codici sentinella)  
> **Obiettivo**: Rispettare i limiti del contratto e collaudare casi tipici e anomali.

## Obiettivo
Scrivere una funzione pura che calcoli il prezzo finale scontato, verificando la validità percentuale.

## Il Contratto Software
```python
def calcola_prezzo_scontato(prezzo: float, percentuale: float) -> float:
    """
    Calcola il prezzo finale dopo aver applicato lo sconto percentuale.

    Argomenti:
        prezzo: Valore monetario >= 0.
        percentuale: Percentuale compresa tra 0.0 e 100.0.

    Ritorna:
        Il prezzo scontato, oppure -1.0 se i dati in ingresso non sono validi.
    """
```

## Istruzioni
1. Controlla la validità: se `prezzo < 0` o `percentuale < 0` o `percentuale > 100`, restituisci `-1.0`.
2. Calcola l'importo dello sconto: $sconto = (prezzo \times percentuale) / 100$.
3. Restituisci il prezzo finale: `return prezzo - sconto`.
4. Nel `main()`: chiedi i dati, chiama la funzione e segnala se i dati inseriti non erano validi.

## Esempio di Esecuzione
```text
Prezzo originale: 100.0
Percentuale di sconto: 20.0
Prezzo scontato: 80.00€
```
