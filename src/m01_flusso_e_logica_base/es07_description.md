# Esercizio 07: Equazione di Primo Grado ax + b = 0

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Condizioni annidate, divisione ed espressioni algebriche)  
> **Obiettivo**: Analizzare le casistiche speciali (divisione per zero, forma indeterminata, forma impossibile).

## Obiettivo
Risolvere l'equazione lineare $ax + b = 0$, dati i due coefficienti reali $a$ e $b$.

## Regole Matematiche
- Se $a = 0$ e $b = 0$: l'equazione diventa $0x = 0$ $\to$ **indeterminata** (infinite soluzioni).
- Se $a = 0$ e $b \neq 0$: l'equazione diventa $0x = -b$ $\to$ **impossibile** (nessuna soluzione).
- Se $a \neq 0$: l'equazione ha una sola soluzione calcolabile con $x = -b / a$.

## Istruzioni
1. Chiedi i coefficienti decimali `a: float` e `b: float`.
2. Gestisci il caso $a = 0$ distinguendo se $b$ è nullo oppure no.
3. Se $a \neq 0$, calcola $x$ e mostra il risultato nel formato: `"La soluzione è x = [x]"`.

## Esempio di Esecuzione
```text
Inserisci il coefficiente a: 2
Inserisci il coefficiente b: 4
La soluzione è x = -2.0
```
