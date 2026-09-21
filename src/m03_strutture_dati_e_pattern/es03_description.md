# Esercizio 03: Conversione da Liste Parallele a Tabella di Record

> **Prerequisiti teorici**: Modulo 03 (Cap. 02 - La Struttura Regina: Lista di Dizionari)  
> **Obiettivo**: Comprendere il passaggio storico e metodologico da collezioni separate a record strutturati.

## Obiettivo
Scrivere una funzione che riceva due liste parallele della stessa lunghezza (`nomi` e `voti`) e le converta in un'unica **tabella dati** (lista di dizionari).

## Il Contratto Software
```python
def componi_tabella_studenti(nomi: list[str], voti: list[float]) -> list[dict]:
    """
    Combina due liste parallele in una lista di record studente.
    Ogni record ha il formato: {"nome": str, "voto": float}.
    Se le liste hanno lunghezze differenti, restituisce una lista vuota [].
    """
```

## Istruzioni
1. Verifica se `len(nomi) != len(voti)`: in tal caso, restituisci subito `[]`.
2. Con un ciclo su indici (o tramite `zip`), crea per ogni posizione un dizionario `{"nome": ..., "voto": ...}` e aggiungilo alla lista dei record.
3. Restituisci la tabella completa.

## Esempio di Utilizzo
```python
nomi = ["Alice", "Bob", "Carla"]
voti = [8.5, 7.0, 9.2]

tabella = componi_tabella_studenti(nomi, voti)
print(tabella)
# Output:
# [
#   {"nome": "Alice", "voto": 8.5},
#   {"nome": "Bob", "voto": 7.0},
#   {"nome": "Carla", "voto": 9.2}
# ]
```
