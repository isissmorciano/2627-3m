import json

from .catalogo import libro_disponibile


def presta_libro(libro: dict) -> bool:
    if not libro_disponibile(libro):
        return False
    libro["copie"] -= 1
    return True


def restituisci_libro(libro: dict) -> bool:
    if libro["copie"] < libro["copie_iniziali"]:
        libro["copie"] += 1
        return True
    return False


def salva_archivio(libri: list[dict], percorso: str) -> None:
    with open(percorso, "w", encoding="utf-8") as file:
        json.dump(libri, file, indent=4, ensure_ascii=False)


def carica_archivio(percorso: str) -> list[dict]:
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
