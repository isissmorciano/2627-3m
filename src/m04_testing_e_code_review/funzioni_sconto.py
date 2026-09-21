def calcola_prezzo_scontato(prezzo: float, percentuale: float) -> float:
    """Calcola il prezzo finale dopo lo sconto."""
    if prezzo < 0 or percentuale < 0 or percentuale > 100:
        return -1.0
    quota_sconto = (prezzo * percentuale) / 100.0
    return prezzo - quota_sconto
