def conta_frequenze_categorie(prodotti: list[dict]) -> dict[str, int]:
    """Conta quanti prodotti appartengono a ogni categoria."""
    frequenze: dict[str, int] = {}

    for p in prodotti:
        cat = p["categoria"]
        if cat in frequenze:
            frequenze[cat] += 1
        else:
            frequenze[cat] = 1

    return frequenze


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
        {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    ]

    statistiche = conta_frequenze_categorie(catalogo)
    print("Statistiche per categoria:")
    for cat, num in statistiche.items():
        print(f"- {cat}: {num} articoli")


if __name__ == "__main__":
    main()
