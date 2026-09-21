import json


def crea_tabellone() -> dict:
    return {"totale": 0, "corrette": 0}


def registra_esito(tabellone: dict, successo: bool) -> None:
    tabellone["totale"] += 1
    if successo:
        tabellone["corrette"] += 1


def calcola_percentuale(tabellone: dict) -> float:
    if tabellone["totale"] == 0:
        return 0.0
    return round((tabellone["corrette"] / tabellone["totale"]) * 100.0, 1)


def salva_risultati(tabellone: dict, percorso: str) -> None:
    with open(percorso, "w", encoding="utf-8") as file:
        json.dump(tabellone, file, indent=4)


def carica_risultati(percorso: str) -> dict:
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return crea_tabellone()
