# Esercizio 09: Equazione di Secondo Grado ax² + bx + c = 0

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Modulo standard `math`, calcolo potenze `**`, radice quadrata)  
> **Obiettivo**: Applicare la formula risolutiva completa per il calcolo delle radici reali.

## Obiettivo
Risolvere l'equazione di secondo grado $ax^2 + bx + c = 0$, dati i tre coefficienti reali $a, b, c$ (con $a \neq 0$).

## Regole Matematiche
Calcola il discriminante: $\Delta = b^2 - 4ac$.
- Se $\Delta > 0$: esistono due soluzioni reali distinte:
  $$x_1 = \frac{-b + \sqrt{\Delta}}{2a}, \quad x_2 = \frac{-b - \sqrt{\Delta}}{2a}$$
- Se $\Delta = 0$: esiste una soluzione reale doppia:
  $$x = \frac{-b}{2a}$$
- Se $\Delta < 0$: non ci sono soluzioni reali.

## Istruzioni
1. Importa la libreria standard `math` per poter usare `math.sqrt()`.
2. Chiedi i coefficienti decimali `a`, `b` e `c`.
3. Calcola il discriminante $\Delta$.
4. Stampa il messaggio o le soluzioni formattate corrispondenti:
   - Due soluzioni: `"Le soluzioni sono x1 = [x1] e x2 = [x2]"`
   - Soluzione doppia: `"La soluzione doppia è x = [x]"`
   - Nessuna soluzione: `"Non ci sono soluzioni reali."`

## Esempio di Esecuzione
```text
Inserisci il coefficiente a: 1
Inserisci il coefficiente b: 0
Inserisci il coefficiente c: -4
Le soluzioni sono x1 = 2.0 e x2 = -2.0
```
