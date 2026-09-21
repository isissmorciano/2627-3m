# Esercizio 06: Package Biblioteca con Prestiti e Persistenza

> **Prerequisiti teorici**: Modulo 03 (Cap. 02, 05, 07, 08 - Integrazione finale di funzioni, package e file)  
> **Obiettivo**: Realizzare un package gestionale completo che modella libri, disponibilità e prestiti.

## Struttura Richiesta
```text
biblioteca/
├── __init__.py
├── catalogo.py     <-- Crea libri, filtra per genere, verifica copie
└── prestiti.py     <-- Presta, restituisce e salva l'archivio su JSON
```

## Specifiche del Modulo `catalogo.py`:
- `crea_libro(titolo: str, autore: str, genere: str, copie: int) -> dict`:  
  Restituisce `{"titolo": ..., "autore": ..., "genere": ..., "copie": copie, "copie_iniziali": copie}`.
- `libro_disponibile(libro: dict) -> bool`:  
  Restituisce `True` se `libro["copie"] > 0`.
- `filtra_per_genere(libri: list[dict], genere: str) -> list[dict]`

## Specifiche del Modulo `prestiti.py`:
- `presta_libro(libro: dict) -> bool`:  
  Se disponibile, decrementa `libro["copie"]` e restituisce `True`. Altrimenti `False`.
- `restituisci_libro(libro: dict) -> bool`:  
  Se `libro["copie"] < libro["copie_iniziali"]`, incrementa e restituisce `True`. Altrimenti `False`.
- `salva_archivio(libri: list[dict], percorso: str) -> None`
- `carica_archivio(percorso: str) -> list[dict]`
