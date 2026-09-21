# Esercizio 05: Pattern di Filtraggio (Filter)

> **Prerequisiti teorici**: Modulo 05 (Cap. 03 - I 4 Pattern Fondamentali: Filtraggio)  
> **Obiettivo**: Selezionare un sottoinsieme di record che soddisfa un criterio, preservando la lista originale.

## Obiettivo
Scrivere una funzione `filtra_per_categoria(prodotti: list[dict], categoria: str) -> list[dict]` che estrae solo i prodotti appartenenti alla categoria richiesta (confronto *case-insensitive*).

## Il Contratto Software
- Riceve la lista `prodotti` e la stringa `categoria`.
- Crea una nuova lista `selezionati: list[dict] = []`.
- Aggiunge solo i record la cui chiave `"categoria"` corrisponde a quella cercata (usando `.lower()` per ignorare maiuscole/minuscole).
- Restituisce la nuova lista (che sarà vuota `[]` se nessun prodotto soddisfa il filtro).

## Esempio di Utilizzo
```python
libri = filtra_per_categoria(catalogo, "libri")
print(len(libri))  # 1
print(libri[0]["nome"])  # "Manuale Python"
```
