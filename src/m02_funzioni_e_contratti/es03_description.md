# Esercizio 03: Parametri Opzionali - Formattazione Saluto

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Parametri con valore di default)  
> **Obiettivo**: Progettare funzioni flessibili che funzionano con o senza parametri secondari.

## Obiettivo
Scrivere una funzione che generi una stringa di saluto formale o informale, utilizzando un parametro di default per il titolo di cortesia.

## Il Contratto Software
```python
def genera_saluto(nome: str, cognome: str, titolo: str = "Sig./Sig.ra") -> str:
    """
    Costruisce una formula di benvenuto personalizzata.

    Argomenti:
        nome: Nome della persona.
        cognome: Cognome della persona.
        titolo: Titolo di cortesia (default: "Sig./Sig.ra").

    Ritorna:
        Stringa formattata: "Benvenuto/a <titolo> <nome> <cognome>!"
    """
```

## Istruzioni
1. La funzione deve combinare i parametri in un'unica stringa senza effettuare stampe.
2. Nel `main()`, mostra che la funzione può essere chiamata sia con 2 argomenti (usando il default) sia sovrascrivendo il terzo parametro (es. `"Dott."`).

## Esempio di Esecuzione
```text
Chiamata con default: Benvenuto/a Sig./Sig.ra Mario Rossi!
Chiamata con titolo:  Benvenuto/a Dott.ssa Laura Bianchi!
```
