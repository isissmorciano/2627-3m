# Esercizio 02: Smascherare i Bug sui Casi di Confine

> **Prerequisiti teorici**: Modulo 04 (Cap. 02 - La Matrice dei Casi di Prova)  
> **Obiettivo**: Individuare bug nascosti generati da un uso errato dei connettori `<` anziché `<=`.

## La Specifica Ufficiale
La funzione `valuta_voto(media: float) -> str` deve rispettare questo contratto:
- `media >= 8.0`: `"Ottimo"`
- `6.0 <= media < 8.0`: `"Sufficiente"`
- `0.0 <= media < 6.0`: `"Insufficiente"`
- Fuori range ($< 0$ o $> 10$): `"Non Valido"`

## Il Tranello
Un collega ha scritto questa implementazione contenente un bug sui casi di confine:
```python
def valuta_voto_difettosa(media: float) -> str:
    if media < 0 or media > 10:
        return "Non Valido"
    if media > 8.0:  # <-- TRANELLO: ha usato > invece di >=
        return "Ottimo"
    if media >= 6.0:
        return "Sufficiente"
    return "Insufficiente"
```

## Istruzioni
Scrivi la suite di test nel tuo file `es02_student.py`:
1. `test_caso_tipico()`: media `7.0` deve dare `"Sufficiente"`.
2. `test_confine_esatto_ottimo()`: collauda il valore critico `8.0`.
   - Se il test asserisce `valuta_voto_difettosa(8.0) == "Ottimo"`, **questo test DEVE fallire**, smascherando il bug del collega!
3. Scrivi nel file `es02_corretta.py` la versione corretta della funzione e dimostra che supera tutti i test al 100% verde.
