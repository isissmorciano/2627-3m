# Esercizio 01: I Tuoi Primi Test Unitari con assert

> **Prerequisiti teorici**: Modulo 04 (Cap. 03 - Unit Testing con Pytest)  
> **Obiettivo**: Imparare a scrivere funzioni di test autonome con la parola chiave `assert`.

## Obiettivo
In questo esercizio il codice applicativo ti viene già fornito nel modulo `funzioni_sconto.py`. Il tuo compito è scrivere il file di test `es01_student.py` (o `test_sconto.py`).

## Il Codice da Testare (`funzioni_sconto.py`)
```python
def calcola_prezzo_scontato(prezzo: float, percentuale: float) -> float:
    """Calcola il prezzo finale dopo aver applicato lo sconto."""
    if prezzo < 0 or percentuale < 0 or percentuale > 100:
        return -1.0
    sconto = (prezzo * percentuale) / 100.0
    return prezzo - sconto
```

## Istruzioni
Nel tuo file di test devi definire almeno 3 funzioni che iniziano con `test_`:
1. `test_sconto_normale()`: verifica che con `prezzo=100.0` e `percentuale=20.0` il risultato sia esattamente `80.0`.
2. `test_sconto_zero()`: verifica il caso limite in cui lo sconto è `0.0%` (il prezzo deve rimanere identico).
3. `test_sconto_totale()`: verifica il caso limite in cui lo sconto è `100.0%` (il prezzo deve diventare `0.0`).
4. `test_dati_non_validi()`: verifica che un prezzo negativo o uno sconto oltre `100` restituisca il codice di errore `-1.0`.

Lancia il test da terminale con:
```bash
pytest src/m04_testing_e_code_review/es01_student.py
```
