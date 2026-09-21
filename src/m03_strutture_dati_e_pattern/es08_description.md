# Esercizio 08: Conteggio delle Frequenze

> **Prerequisiti teorici**: Modulo 05 (Cap. 04 - Pattern Dizionari: Frequenze)  
> **Obiettivo**: Costruire un dizionario istogramma contando le occorrenze di chiavi/categorie.

## Obiettivo
Scrivere una funzione `conta_frequenze_categorie(prodotti: list[dict]) -> dict[str, int]` che conta quanti prodotti sono presenti per ciascuna categoria.

## Il Contratto Software
- Inizializza un dizionario vuoto: `frequenze: dict[str, int] = {}`.
- Scorri i record:
  - Se la categoria è già presente nel dizionario, incrementa il suo contatore di 1 (`frequenze[cat] += 1`).
  - Altrimenti, inizializzala a 1 (`frequenze[cat] = 1`).
- Restituisce il dizionario delle occorrenze.

## Esempio di Utilizzo
```python
conteggi = conta_frequenze_categorie(catalogo)
print(conteggi)
# Output: {'Informatica': 2, 'Libri': 1, 'Arredamento': 1}
```
