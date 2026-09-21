# Esercizio 04: Pattern di Ricerca Univoca (Find)

> **Prerequisiti teorici**: Modulo 05 (Cap. 03 - I 4 Pattern Fondamentali: Ricerca)  
> **Obiettivo**: Individuare un singolo record specifico o gestire l'assenza con `None`.

## Obiettivo
Scrivere una funzione `trova_prodotto_per_id(prodotti: list[dict], id_cercato: int) -> dict | None`.

## Il Contratto Software
- Cerca nella lista `prodotti` il dizionario il cui valore di `"id"` è uguale a `id_cercato`.
- **Uscita immediata (*Early Return*):** appena il prodotto viene trovato, restituiscilo subito (`return p`) interrompendo il ciclo.
- Se il ciclo termina senza trovare corrispondenze, restituisci `None`.

## Esempio di Utilizzo
```python
p = trova_prodotto_per_id(catalogo, 103)
print(p["nome"])  # "Manuale Python"

inesistente = trova_prodotto_per_id(catalogo, 999)
print(inesistente)  # None
```
