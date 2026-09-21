def tieni_solo_positivi_sicura(numeri: list[int]) -> list[int]:
    """Crea una nuova lista senza alterare quella di partenza."""
    risultato: list[int] = []
    for n in numeri:
        if n >= 0:
            risultato.append(n)
    return risultato


def test_risultato_corretto():
    dati = [10, -2, 5, -8, 20]
    assert tieni_solo_positivi_sicura(dati) == [10, 5, 20]


def test_nessuna_alterazione_originale():
    """Verifica che la lista passata resti intatta al 100%."""
    dati_iniziali = [10, -2, 5, -8, 20]
    copia_controllo = dati_iniziali.copy()

    tieni_solo_positivi_sicura(dati_iniziali)

    assert dati_iniziali == copia_controllo
