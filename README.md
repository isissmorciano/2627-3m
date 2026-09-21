# 2627-3m

Esercizi di programmazione Python organizzati in moduli.

## Struttura di un esercizio

Ogni esercizio `esXX` dispone di questi file nella cartella del modulo:

- `esXX_description.md`: testo dell'esercizio.
- `esXX_student.py`: file in cui lo studente deve scrivere la soluzione.
- `esXX_reference.py`: soluzione del docente, quando disponibile.

Moduli disponibili:

- `src/m01_flusso_e_logica_base/`
- `src/m02_funzioni_e_contratti/` (7 esercizi)

I file `student` sono volutamente vuoti all'inizio. Le soluzioni complete sono nei file `reference`.

## Progressione del Modulo 02

Gli esercizi seguono una difficoltà crescente:

1. Area del triangolo: funzione pura e `return` di un valore scalare.
2. Calcolo dello sconto: validazione con valore sentinella.
3. Saluto personalizzato: parametro con valore di default.
4. Geometria del rettangolo: ritorno multiplo tramite tupla.
5. Calcolatrice modulare: separazione dei compiti e `float | None`.
6. Calcolatore BMI: scomposizione top-down a tre strati.
7. Conversioni: modulo locale e `if __name__ == "__main__"`.

## Installazione

Il progetto usa Python 3 e `pytest` per eseguire i test:

```bash
python -m pip install pytest
```

## Test degli studenti

I test degli studenti verificano l'implementazione presente nei file `esXX_student.py`.

Per eseguire tutti i test degli studenti di un modulo:

```bash
python -m pytest tests/test_m01_flusso
python -m pytest tests/test_m02_funzioni
```

Per eseguire tutti i test degli studenti:

```bash
python -m pytest tests/test_m01_flusso tests/test_m02_funzioni
```

Per eseguire i test di un singolo esercizio:

```bash
python -m pytest tests/test_m01_flusso/test_es01.py
python -m pytest tests/test_m02_funzioni/test_es01.py
```

Sostituisci `es01` con l'esercizio desiderato.

## Test delle soluzioni docente

I test reference verificano le soluzioni complete presenti nei file `esXX_reference.py`.

Per eseguire tutti i test reference di un modulo:

```bash
python -m pytest tests/test_m01_flusso_reference
python -m pytest tests/test_m02_funzioni_reference
```

Per eseguire tutti i test delle soluzioni docente:

```bash
python -m pytest tests/test_m01_flusso_reference tests/test_m02_funzioni_reference
```

Per eseguire il test reference di un singolo esercizio:

```bash
python -m pytest tests/test_m01_flusso_reference/test_es01.py
python -m pytest tests/test_m02_funzioni_reference/test_es01.py
```

## Nota

Il comando `pytest` senza percorso esegue anche i test degli studenti. Poiché i file `student` sono vuoti prima dello svolgimento degli esercizi, per verificare solo le soluzioni complete usa i test nelle cartelle `*_reference`.
