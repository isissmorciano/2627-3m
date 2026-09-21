# Esercizio 01: Funzione Pura - Area del Triangolo

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Funzioni come contratti, Type Hints, `return` vs `print`)  
> **Obiettivo**: Scrivere una funzione pura con firma esplicita e un singolo valore di ritorno.

## Obiettivo
Scrivere una funzione che calcoli l'area di un triangolo senza stampare nulla a video, restituendo il risultato a chi la chiama.

## Il Contratto Software
Definisci la funzione:
```python
def calcola_area_triangolo(base: float, altezza: float) -> float:
    """
    Calcola l'area di un triangolo.

    Argomenti:
        base: Lunghezza positiva della base.
        altezza: Lunghezza positiva dell'altezza.

    Ritorna:
        L'area del triangolo.
    """
```

## Istruzioni
1. La funzione `calcola_area_triangolo` **NON deve fare né `input()` né `print()`**.
2. Calcola l'area con la formula $area = (base \times altezza) / 2$.
3. Restituisci un singolo valore con `return`.
3. Nel `main()`:
   - Chiedi all'utente `base` e `altezza`.
    - Chiama la funzione.
    - Stampa il risultato formattato con due decimali (`:.2f`).

## Esempio di Esecuzione
```text
Inserisci la base: 5.0
Inserisci l'altezza: 3.0
Area del triangolo: 7.50
```
