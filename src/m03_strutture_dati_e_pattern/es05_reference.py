def filtra_per_categoria(prodotti: list[dict], categoria: str) -> list[dict]:
    """Estrae una nuova lista di record appartenenti alla categoria indicata."""
    selezionati: list[dict] = []
    categoria_target = categoria.lower()

    for p in prodotti:
        if p["categoria"].lower() == categoria_target:
            selezionati.append(p)

    return selezionati


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
        {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    ]

    informatica = filtra_per_categoria(catalogo, "Informatica")
    print(f"Prodotti informatica trovati: {len(informatica)}")
    for item in informatica:
        print(f"- {item['nome']} ({item['prezzo']}€)")


if __name__ == "__main__":
    main()
