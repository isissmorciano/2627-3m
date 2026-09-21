# Esercizio 02: Gestione Archivio Studenti in Formato JSON

> **Prerequisiti teorici**: Modulo 03 (Cap. 07 - JSON con `json.dump` e `json.load`)  
> **Obiettivo**: Serializzare e deserializzare liste di dizionari con gestione dei file corrotti.

## Obiettivo
Creare due funzioni per salvare e ricaricare l'archivio studenti in formato JSON.

## Il Contratto Software
1. `salva_studenti(studenti: list[dict], percorso: str) -> bool`:
   Salva la lista di dizionari formattata con `indent=4` ed `encoding="utf-8"`. Restituisce `True` se il salvataggio è andato a buon fine, `False` in caso di `IOError`.
2. `carica_studenti(percorso: str) -> list[dict]`:
   Carica e restituisce la lista di record da JSON.  
   **Gestione Difensiva:** Se il file non esiste (`FileNotFoundError`) o se il contenuto non è un JSON valido (`json.JSONDecodeError`), intercetta l'eccezione e restituisce una lista vuota `[]`.

## Esempio di Utilizzo
```python
studenti = [{"nome": "Alice", "classe": "3A", "media": 8.5}, {"nome": "Bob", "classe": "3B", "media": 7.0}]

salva_studenti(studenti, "studenti.json")
dati_caricati = carica_studenti("studenti.json")
print(len(dati_caricati))  # 2
```
