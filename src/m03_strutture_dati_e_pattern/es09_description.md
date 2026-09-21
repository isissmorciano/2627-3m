# Esercizio 09: Raggruppamento per Categoria (Grouping)

> **Prerequisiti teorici**: Modulo 05 (Cap. 04 - Pattern Dizionari: Grouping)  
> **Obiettivo**: Riorganizzare una lista piatta in un dizionario in cui ogni valore è una lista di record omogenei.

## Obiettivo
Scrivere una funzione `raggruppa_per_categoria(prodotti: list[dict]) -> dict[str, list[dict]]` che organizza i record in liste tematiche indicizzate per categoria.

## Il Contratto Software
- Inizializza `gruppi: dict[str, list[dict]] = {}`.
- Per ogni prodotto:
  - Se la categoria non è ancora presente tra le chiavi del dizionario, crea una lista vuota: `gruppi[cat] = []`.
  - Aggiungi il prodotto alla lista corrispondente: `gruppi[cat].append(p)`.
- Restituisci il dizionario dei gruppi.

## Esempio di Utilizzo
```python
gruppi = raggruppa_per_categoria(catalogo)

print(len(gruppi["Informatica"]))  # 2
for p in gruppi["Informatica"]:
    print(f"- {p['nome']}")
```
