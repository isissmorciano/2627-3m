# Esercizio 10: Triangolo Rettangolo e Precisione Floating-Point

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Funzione `max()`, funzione `abs()`, tolleranza numerica)  
> **Obiettivo**: Confrontare valori decimali senza cadere negli errori di arrotondamento floating-point.

## Obiettivo
Dati tre lati positivi di un triangolo, verificare se soddisfano il Teorema di Pitagora.

## Principio Fisico-Matematico e Tolleranza
Nei calcolatori, numeri come $0.1$ o radici non sono sempre esatti in binario. Per confrontare se due float $A$ e $B$ sono uguali, non si usa `A == B`, ma si verifica se la loro differenza in valore assoluto è inferiore a una tolleranza piccolissima (es. `1e-6` = $0.000001$):
```python
abs(ipotenusa**2 - somma_quadrati_cateti) < 1e-6
```

## Istruzioni
1. Chiedi all'utente la lunghezza dei tre lati: `lato1`, `lato2`, `lato3` (`float`).
2. Individua l'ipotenusa usando `max(lato1, lato2, lato3)`.
3. Calcola la somma dei quadrati degli altri due lati (i cateti).
4. Confronta il quadrato dell'ipotenusa con la somma dei quadrati dei cateti usando la tolleranza `1e-6`.
5. Stampa:
   - `"Il triangolo è rettangolo."` oppure
   - `"Il triangolo non è rettangolo."`

## Esempio di Esecuzione
```text
Inserisci la lunghezza del primo lato: 3
Inserisci la lunghezza del secondo lato: 4
Inserisci la lunghezza del terzo lato: 5
Il triangolo è rettangolo.
```
