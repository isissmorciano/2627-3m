# Esercizio 07: Registro della Classe

> **Obiettivo**: Scorrere un dizionario di dizionari e calcolare una media per ciascuno.

Scrivi un programma con la sola funzione `main()` che usa questo registro:

```python
registro = {
    "Alice": {"Italiano": 8.0, "Matematica": 7.0},
    "Marco": {"Italiano": 6.0, "Matematica": 9.0, "Informatica": 9.0},
    "Sara": {},
}
```

Per ogni studente, nell'ordine del registro, calcola e stampa la media dei
voti con due cifre decimali. Se lo studente non ha voti, stampa
`<nome>: nessun voto` invece della media. Usa cicli per scorrere i dizionari,
senza definire altre funzioni oltre a `main()`.

## Esempio di esecuzione

```text
Alice: 7.50
Marco: 8.00
Sara: nessun voto
```
