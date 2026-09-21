def crea_domanda(testo: str, opzioni: list[str], indice_corretto: int) -> dict:
    return {"testo": testo, "opzioni": opzioni, "risposta_esatta": indice_corretto}


def verifica_risposta(domanda: dict, risposta_utente: int) -> bool:
    return risposta_utente == domanda["risposta_esatta"]
