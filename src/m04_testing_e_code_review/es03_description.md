# Esercizio 03: Testare la Mutabilità e l'Integrità dei Dati

> **Prerequisiti teorici**: Modulo 03 (Cap. 05 - Mutabilità) e Modulo 04 (Cap. 04 - Code Review)  
> **Obiettivo**: Scrivere un test che verifica che una funzione non sporchi o modifichi i dati di partenza.

## Il Problema
Spesso una funzione sembra funzionare perché restituisce il valore atteso, ma **danneggia la memoria di chi l'ha chiamata** alterando la lista di partenza.

## Il Codice Sospetto (`filtro_dati.py`)
```python
def tieni_solo_positivi_bug(numeri: list[int]) -> list[int]:
    for n in numeri:
        if n < 0:
            numeri.remove(n)  # MODIFICA DISTRUTTIVA IN-PLACE!
    return numeri
```

## Il Tuo Compito da Detective
Scrivi una funzione di test `test_nessuna_alterazione_originale()` che:
1. Crea una lista `dati_iniziali = [10, -2, 5, -8, 20]`.
2. Crea una copia di sicurezza identica: `copia_controllo = dati_iniziali.copy()`.
3. Chiama la funzione con `dati_iniziali`.
4. Fa un'asserzione: `assert dati_iniziali == copia_controllo`.
5. Esegui il test: vedrai Pytest fallire immediatamente, provando che la funzione è difettosa e non sicura!
