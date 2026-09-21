import json


def salva_studenti(studenti: list[dict], percorso: str) -> bool:
    """Salva una lista di studenti in formato JSON indentato."""
    try:
        with open(percorso, "w", encoding="utf-8") as file:
            json.dump(studenti, file, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False


def carica_studenti(percorso: str) -> list[dict]:
    """Carica gli studenti da JSON. Restituisce [] se assente o corrotto."""
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            dati = json.load(file)
            if isinstance(dati, list):
                return dati
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def main() -> None:
    studenti = [
        {"nome": "Alice", "classe": "3A", "media": 8.5},
        {"nome": "Bob", "classe": "3B", "media": 7.0},
    ]

    file_archivio = "studenti.json"
    salva_studenti(studenti, file_archivio)
    print(f"Dati salvati su {file_archivio}")

    recuperati = carica_studenti(file_archivio)
    print(f"Recuperati {len(recuperati)} record con successo.")


if __name__ == "__main__":
    main()
