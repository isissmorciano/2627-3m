def crea_libro(titolo: str, autore: str, genere: str, copie: int) -> dict:
    return {
        "titolo": titolo,
        "autore": autore,
        "genere": genere,
        "copie": copie,
        "copie_iniziali": copie,
    }


def libro_disponibile(libro: dict) -> bool:
    return libro["copie"] > 0


def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    return [libro for libro in libri if libro["genere"].lower() == genere.lower()]
