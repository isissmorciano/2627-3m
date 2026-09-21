# Esercizio 06: Metodologia Top-Down - Calcolatore BMI

> **Prerequisiti teorici**: Modulo 03 (Cap. 04 - La Scomposizione Top-Down a 3 Strati)  
> **Obiettivo**: Realizzare un'applicazione separando rigorosamente: Strato I/O, Strato Logica Pura e Strato Presentazione.

## Lo Schema Architetturale a 3 Strati

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. STRATO I/O (Input con validazione)                       │
│    chiedi_peso() -> float                                   │
│    chiedi_altezza() -> float                                │
├─────────────────────────────────────────────────────────────┤
│ 2. STRATO LOGICA PURA (Il Cervello - Niente print!)          │
│    calcola_bmi(peso, altezza) -> float                      │
│    classifica_bmi(bmi) -> str                               │
├─────────────────────────────────────────────────────────────┤
│ 3. STRATO PRESENTAZIONE (La Voce)                           │
│    stampa_report_bmi(peso, altezza, bmi, categoria) -> None │
└─────────────────────────────────────────────────────────────┘
```

## Categorie di Riferimento BMI ($BMI = peso / altezza^2$)
- $BMI < 18.5$: `"Sottopeso"`
- $18.5 \le BMI < 25.0$: `"Normopeso"`
- $25.0 \le BMI < 30.0$: `"Sovrappeso"`
- $BMI \ge 30.0$: `"Obesità"`

## Istruzioni
1. **Strato 1 (I/O)**: `chiedi_peso()` e `chiedi_altezza()` usano un ciclo `while` per rifiutare valori non positivi.
2. **Strato 2 (Logica)**: `calcola_bmi` e `classifica_bmi` prendono parametri e fanno `return`. Non contengono `print()`.
3. **Strato 3 (Presentazione)**: `stampa_report_bmi` formatta la scheda finale.
4. **`main()`**: Richiama le funzioni nell'ordine logico.

## Esempio di Esecuzione
```text
Inserisci il peso in kg: 70.0
Inserisci l'altezza in metri: 1.75

=== SCHEDA DI VALUTAZIONE BMI ===
Peso inserito:    70.0 kg
Altezza inserita: 1.75 m
Valore BMI:       22.86
Classificazione:  Normopeso
=================================
```
