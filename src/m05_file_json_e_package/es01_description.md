# Esercizio 01: Scrittura, Lettura e Gestione Eccezioni su File di Testo

> **Prerequisiti teorici**: Modulo 03 (Cap. 06 - Gestione Eccezioni, Cap. 07 - File con `with open`)  
> **Obiettivo**: Scrivere e leggere file `.txt` gestendo in modo pulito l'errore `FileNotFoundError`.

## Obiettivo
Scrivere due funzioni pure per la persistenza di elenchi di stringhe su file di testo:
1. `scrivi_righe(righe: list[str], percorso: str) -> None`:
   Apre il file in modalità scrittura (`"w"` con `encoding="utf-8"`) e scrive ogni elemento su una riga separata.
2. `leggi_righe(percorso: str) -> list[str]`:
   Apre il file in lettura (`"r"` con `encoding="utf-8"`), rimuove gli spazi e caratteri di a capo (`.strip()`) e restituisce la lista di righe.  
   **Attenzione:** Se il file non esiste, deve intercettare l'eccezione `FileNotFoundError` e restituire una lista vuota `[]` senza far crashare il programma!

## Esempio di Utilizzo
```python
note = ["Comprare il latte", "Studiare Python", "Fare il commit su Git"]
scrivi_righe(note, "promemoria.txt")

lette = leggi_righe("promemoria.txt")
print(lette)  # ['Comprare il latte', 'Studiare Python', 'Fare il commit su Git']

inesistenti = leggi_righe("file_fantasma.txt")
print(inesistenti)  # [] (Nessun crash!)
```
