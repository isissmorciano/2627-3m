# Progetto 02: Campionato Football Analyzer da JSON

> **Prerequisiti teorici**: Modulo 03 (File JSON, Dizionari) e Modulo 05 (Grouping, Statistiche)  
> **Obiettivo**: Elaborare un dataset reale di partite per calcolare statistiche di squadra e podio.

## Lo Scenario
Hai a disposizione il file `partite.json` contenente i risultati della stagione. Il tuo programma deve estrarre le statistiche per ogni squadra e visualizzare una classifica ordinata per percentuale di vittorie.

### Esempio di struttura di `partite.json`:
```json
[
  {"data": "2026-01-15", "casa": "Milan", "trasferta": "Juventus", "gol_c": 2, "gol_t": 1},
  {"data": "2026-01-16", "casa": "Inter", "trasferta": "Napoli", "gol_c": 3, "gol_t": 2},
  {"data": "2026-01-17", "casa": "Juventus", "trasferta": "Lazio", "gol_c": 1, "gol_t": 1},
  {"data": "2026-01-18", "casa": "Milan", "trasferta": "Roma", "gol_c": 2, "gol_t": 0}
]
```

## Funzioni Richieste (Tutte Pure tranne le stampe)

1. `carica_partite(percorso: str) -> list[dict]`
2. `estrai_squadre_uniche(partite: list[dict]) -> list[str]`: restituisce la lista delle squadre senza duplicati.
3. `filtra_partite_squadra(partite: list[dict], squadra: str) -> list[dict]`: estrae tutte le partite giocate da quella squadra (in casa o in trasferta).
4. `analizza_prestazioni(partite: list[dict], squadra: str) -> dict`: calcola per la squadra un dizionario riassuntivo con:
   - `"partite_giocate"`: `int`
   - `"vittorie"`: `int`
   - `"pareggi"`: `int`
   - `"sconfitte"`: `int`
   - `"gol_fatti_media"`: `float`
   - `"gol_subiti_media"`: `float`
   - `"percentuale_vittorie"`: `float` (tra 0 e 100)
5. `stampa_tabella_statistiche(statistiche: list[dict]) -> None`
