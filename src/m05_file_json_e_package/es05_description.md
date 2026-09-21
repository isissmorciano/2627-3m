# Esercizio 05: Package Quiz e Modulo Risultati JSON

> **Prerequisiti teorici**: Modulo 03 (Cap. 07, 08 - Architettura a moduli e persistenza dati)  
> **Obiettivo**: Separare la logica delle domande da quella del salvataggio e recupero dello score.

## Struttura della Cartella
```text
quiz/
├── __init__.py
├── domande.py
└── risultati.py
```

## Modulo 1: `quiz/domande.py`
- `crea_domanda(testo: str, opzioni: list[str], indice_corretto: int) -> dict`
- `verifica_risposta(domanda: dict, risposta_utente: int) -> bool`

## Modulo 2: `quiz/risultati.py`
- `crea_tabellone() -> dict`: restituisce `{"totale": 0, "corrette": 0}`.
- `registra_esito(tabellone: dict, successo: bool) -> None`
- `calcola_percentuale(tabellone: dict) -> float`
- `salva_risultati(tabellone: dict, percorso: str) -> None`: salva lo score in JSON.
- `carica_risultati(percorso: str) -> dict`: carica lo score da JSON o restituisce un tabellone nuovo.
