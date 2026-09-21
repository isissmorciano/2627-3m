# Esercizio 04: Funzione Pura - Geometria del Rettangolo

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Funzioni come contratti, Type Hints, `return` vs `print`)  
> **Obiettivo**: Restituire più risultati da una funzione tramite una tupla.

## Obiettivo
Scrivere una funzione che calcoli area e perimetro di un rettangolo senza stampare nulla a video, restituendo entrambi i valori a chi la chiama.

## Il Contratto Software

```python
def calcola_rettangolo(base: float, altezza: float) -> tuple[float, float]:
    """Calcola area e perimetro di un rettangolo."""
```

## Istruzioni
1. La funzione `calcola_rettangolo` **NON deve fare né `input()` né `print()`**.
2. Calcola $area = base \times altezza$ e $perimetro = 2 \times (base + altezza)$.
3. Restituisci la coppia di valori come tupla: `return area, perimetro`.
4. Nel `main()`, chiedi i dati, spacchetta il risultato e stampa i valori con due decimali.

## Esempio di Esecuzione
```text
Inserisci la base: 5.0
Inserisci l'altezza: 3.0
Area: 15.00
Perimetro: 16.00
```
