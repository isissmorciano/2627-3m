def valuta_voto_difettosa(media: float) -> str:
    """Versione difettosa: sbaglia la soglia esatta di 8.0."""
    if media < 0 or media > 10:
        return "Non Valido"
    if media > 8.0:
        return "Ottimo"
    if media >= 6.0:
        return "Sufficiente"
    return "Insufficiente"
