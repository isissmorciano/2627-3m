# Esercizio 10: Indicizzazione Rapida per ID (Lookup O(1))

> **Prerequisiti teorici**: Modulo 05 (Cap. 04 - Pattern Dizionari: Indicizzazione)  
> **Obiettivo**: Convertire una sequenza da scorrere linearmente in una mappa ad accesso istantaneo senza cicli.

## Obiettivo
Scrivere una funzione `crea_indice_per_id(prodotti: list[dict]) -> dict[int, dict]` che trasforma la tabella in una mappa `ID -> Record`.

## Perché è utile?
Per cercare un prodotto in una lista di 1.000.000 di elementi servono in media 500.000 controlli con un ciclo `for`. Se indicizziamo la lista in un dizionario basato sull'ID, il recupero con `indice.get(id)` è **immediato ed è eseguito in un solo passaggio**.

## Il Contratto Software
- Riceve la lista `prodotti`.
- Inizializza `indice: dict[int, dict] = {}`.
- Associa a ciascun ID il rispettivo dizionario prodotto: `indice[p["id"]] = p`.
- Restituisce la mappa completa.

## Esempio di Utilizzo
```python
indice = crea_indice_per_id(catalogo)

# Accesso immediato senza alcun ciclo for!
p103 = indice.get(103)
if p103:
    print(p103["nome"])  # "Manuale Python"
```
