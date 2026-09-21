# Esercizio 04: Package Geometria 2D - Punti e Linee

> **Prerequisiti teorici**: Modulo 03 (Cap. 08 - Package e import relativi con `__init__.py`)  
> **Obiettivo**: Costruire un package con due moduli interdipendenti (`linee` importa da `punti`).

## Struttura del Package
Crea una cartella `coordinate/` organizzata così:
```text
coordinate/
├── __init__.py
├── punti.py
└── linee.py
```

## Modulo 1: `coordinate/punti.py`
- `crea_punto(x: float, y: float) -> dict`: restituisce `{"x": x, "y": y}`.
- `distanza_tra_punti(p1: dict, p2: dict) -> float`: calcola $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ (usa `math.sqrt`).
- `info_punto(punto: dict) -> str`: restituisce ad esempio `"(3.0, 4.0)"`.

## Modulo 2: `coordinate/linee.py`
Questo modulo deve importare dal modulo gemello con un **import relativo**:
```python
from .punti import crea_punto, distanza_tra_punti, info_punto
```
- `crea_linea(p1: dict, p2: dict) -> dict`: restituisce `{"p1": p1, "p2": p2}`.
- `lunghezza_linea(linea: dict) -> float`: usa `distanza_tra_punti` per calcolare la lunghezza.
- `punto_medio(linea: dict) -> dict`: calcola e restituisce il punto medio `((x1+x2)/2, (y1+y2)/2)`.

## Script Principale (`main.py`)
Importa dal package:
```python
from coordinate import linee, punti
```
Crea due punti, traccia la linea e stampa lunghezza e punto medio.
