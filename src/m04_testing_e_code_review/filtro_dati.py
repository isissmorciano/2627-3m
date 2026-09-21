def tieni_solo_positivi_bug(numeri: list[int]) -> list[int]:
    """Versione difettosa che modifica la lista ricevuta in-place."""
    for n in numeri:
        if n < 0:
            numeri.remove(n)
    return numeri
