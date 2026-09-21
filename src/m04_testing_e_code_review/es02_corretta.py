def valuta_voto(media: float) -> str:
    """Restituisce il giudizio gestendo correttamente le soglie esatte."""
    if media < 0.0 or media > 10.0:
        return "Non Valido"
    if media >= 8.0:
        return "Ottimo"
    if media >= 6.0:
        return "Sufficiente"
    return "Insufficiente"
