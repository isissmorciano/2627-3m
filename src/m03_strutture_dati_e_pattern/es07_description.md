# Esercizio 07: Pattern di Aggregazione (Reduce)

> **Prerequisiti teorici**: Modulo 05 (Cap. 03 - I 4 Pattern Fondamentali: Aggregazione)  
> **Obiettivo**: Sintetizzare un'intera tabella di record in un singolo valore scalare o record estremo.

## Obiettivo
Scrivere due funzioni di aggregazione per analizzare i totali del magazzino:
1. `calcola_valore_totale(prodotti: list[dict]) -> float`:
   Calcola e restituisce la somma complessiva dei prezzi di tutti i prodotti. Se la lista è vuota, restituisce `0.0`.
2. `trova_prodotto_piu_costoso(prodotti: list[dict]) -> dict | None`:
   Restituisce l'intero record del prodotto con il prezzo più elevato. Se la lista è vuota, restituisce `None`.

## Esempio di Utilizzo
```python
totale = calcola_valore_totale(catalogo)
print(f"Valore magazzino: {totale:.2f}€")

top_art = trova_prodotto_piu_costoso(catalogo)
if top_art:
    print(f"Top articolo: {top_art['nome']} ({top_art['prezzo']}€)")
```
