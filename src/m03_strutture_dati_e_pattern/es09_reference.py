def raggruppa_per_categoria(prodotti: list[dict]) -> dict[str, list[dict]]:
    """Organizza i prodotti raggruppandoli in liste per categoria."""
    gruppi: dict[str, list[dict]] = {}

    for p in prodotti:
        cat = p["categoria"]
        if cat not in gruppi:
            gruppi[cat] = []
        gruppi[cat].append(p)

    return gruppi


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
        {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    ]

    raggruppati = raggruppa_per_categoria(catalogo)
    for cat, lista_art in raggruppati.items():
        print(f"\nCategoria: {cat} ({len(lista_art)} prodotti)")
        for art in lista_art:
            print(f"  * {art['nome']} -> {art['prezzo']:.2f}€")


if __name__ == "__main__":
    main()
