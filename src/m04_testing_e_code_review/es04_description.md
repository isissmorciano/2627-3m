# Esercizio 04: Laboratorio Code Review - 3 Candidati a Confronto

> **Prerequisiti teorici**: Modulo 04 (Cap. 04 - Laboratorio Code Review)  
> **Obiettivo**: Eseguire una vera sessione di revisione del codice, confrontando tre soluzioni concorrenti e validandole tramite Pytest.

## Lo Scenario
Un cliente chiede una funzione con questo contratto:
> *"Data una lista di studenti `{"nome": str, "voto": float}`, restituire una NUOVA lista contenente SOLO i nomi degli studenti promossi con voto >= 6.0. La lista originale non deve subire modifiche."*

Tre programmatori propongono tre soluzioni:

### Candidato 1 (Distruttivo):
```python
def promo_candidato_1(studenti: list[dict]) -> list[str]:
    nomi = []
    for s in studenti:
        if s["voto"] < 6.0:
            studenti.remove(s)
        else:
            nomi.append(s["nome"])
    return nomi
```

### Candidato 2 (Cieco sui limiti):
```python
def promo_candidato_2(studenti: list[dict]) -> list[str]:
    nomi = []
    for s in studenti:
        if s["voto"] > 6.0:  # Errore: esclude il 6.0 esatto!
            nomi.append(s["nome"])
    return nomi
```

### Candidato 3 (Robusto e Pulito):
```python
def promo_candidato_3(studenti: list[dict]) -> list[str]:
    promossi: list[str] = []
    for s in studenti:
        if s.get("voto", 0.0) >= 6.0:
            promossi.append(s["nome"])
    return promossi
```

## Il Tuo Compito
Scrivi la suite di test `es04_student.py` per:
1. Smascherare il Candidato 1 dimostrando che altera la lista di partenza.
2. Smascherare il Candidato 2 sul caso di confine del voto `6.0`.
3. Dimostrare che il Candidato 3 supera entrambi i test e rispetta le specifiche.
