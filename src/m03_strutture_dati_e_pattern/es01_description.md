# Esercizio 01: Liste e Protezione dei Dati Originali

> **Prerequisiti teorici**: Modulo 03 (Cap. 05 - Mutabilità e Dati Protetti)  
> **Obiettivo**: Implementare una funzione che filtra una lista senza alterare la collezione di partenza (evitare side-effects).

## Obiettivo
Scrivere una funzione pura `rimuovi_negativi(numeri: list[int]) -> list[int]` che riceve una lista di numeri interi e restituisce una **nuova lista** contenente solo i numeri maggiori o uguali a zero ($\ge 0$).

## Regola Aurea del Detective
La funzione **non deve alterare la lista originale**:
- Non usare `.remove()`, `.pop()` o `del` sulla lista passata come parametro.
- Inizializza una nuova lista vuota all'interno della funzione e fai `.append()` solo dei valori positivi o nulli.

## Il Contratto Software
```python
def rimuovi_negativi(numeri: list[int]) -> list[int]:
    """
    Restituisce una nuova lista contenente solo i numeri >= 0.

    Argomenti:
        numeri: Lista di partenza (non viene modificata).

    Ritorna:
        Una nuova lista con i soli valori non negativi.
    """
```

## Esempio di Utilizzo
```python
originali = [8, -3, 12, -7, 0, 5]
puliti = rimuovi_negativi(originali)

print(puliti)  # [8, 12, 0, 5]
print(originali)  # [8, -3, 12, -7, 0, 5] -> Intatta!
```
