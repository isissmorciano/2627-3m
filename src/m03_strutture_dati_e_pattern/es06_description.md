# Esercizio 06: Pattern di Mappatura (Transform / Map)

> **Prerequisiti teorici**: Modulo 05 (Cap. 03 - I 4 Pattern Fondamentali: Mappatura)  
> **Obiettivo**: Trasformare una collezione di record in una nuova lista con dati estratti o ricalcolati.

## Obiettivo
Scrivere due funzioni di trasformazione:
1. `estrai_nomi_prodotti(prodotti: list[dict]) -> list[str]`:
   Restituisce una lista contenente solo i nomi testuali di tutti i prodotti, mantenendo lo stesso ordine.
2. `applica_rincaro(prodotti: list[dict], percentuale: float) -> list[dict]`:
   Restituisce una **nuova lista di record** in cui ogni prodotto ha il prezzo aumentato della percentuale indicata, **senza alterare i prezzi del catalogo di partenza** (usa `.copy()` su ciascun record!).

## Esempio di Utilizzo
```python
nomi = estrai_nomi_prodotti(catalogo)
print(nomi)  # ['Laptop', 'Tastiera', 'Manuale Python', 'Scrivania']

catalogo_aumentato = applica_rincaro(catalogo, 10.0)
print(catalogo[1]["prezzo"])  # 80.0 (intatto)
print(catalogo_aumentato[1]["prezzo"])  # 88.0 (+10%)
```
