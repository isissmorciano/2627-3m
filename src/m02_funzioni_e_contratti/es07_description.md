# Esercizio 07: Modulo Locale e `if __name__ == "__main__"`

> **Prerequisiti teorici**: Modulo 03 (Cap. 08 - Moduli locali, clausola `if __name__ == "__main__"`)
> **Obiettivo**: Separare le funzioni riutilizzabili dal programma principale che le esegue.

## Obiettivo

Usare il modulo locale `conversioni.py` da un programma principale. Le funzioni di conversione devono essere pure e riutilizzabili senza eseguire input o stampe durante l'importazione.

## File richiesti

- `conversioni.py`: modulo con le funzioni pure per convertire temperature e distanze.
- `es07_student.py`: programma principale che importa il modulo e usa le sue funzioni.

## Funzioni richieste in `conversioni.py`

- `celsius_a_fahrenheit(gradi: float) -> float`: formula $(C \times 9/5) + 32$.
- `km_a_miglia(km: float) -> float`: formula $km \times 0.621371$.

Inserisci in fondo a `conversioni.py` un blocco `if __name__ == "__main__":` per eseguire test rapidi solo quando il modulo viene lanciato direttamente.

## Istruzioni per il programma principale

1. Importa le funzioni da `conversioni`.
2. Chiedi all'utente una temperatura in gradi Celsius e una distanza in chilometri.
3. Chiama le funzioni di conversione.
4. Mostra i risultati con un formato leggibile.
5. Inserisci l'avvio del programma dentro `if __name__ == "__main__":`.

## Esempio di Esecuzione

```text
Inserisci temperatura in °C: 0
Inserisci distanza in km: 10
0.0°C equivalgono a 32.0°F
10.00 km equivalgono a 6.21 miglia
```
