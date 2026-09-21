def crea_indice_per_id(prodotti: list[dict]) -> dict[int, dict]:
    """Crea una mappa ID -> Prodotto per accesso immediato."""
    indice: dict[int, dict] = {}
    for p in prodotti:
        indice[p["id"]] = p
    return indice


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
        {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    ]

    indice_prodotti = crea_indice_per_id(catalogo)

    id_scelto = 103
    prodotto = indice_prodotti.get(id_scelto)

    if prodotto:
        print(f"Recupero istantaneo ID {id_scelto}: {prodotto['nome']} ({prodotto['prezzo']}€)")
    else:
        print(f"ID {id_scelto} non presente.")


if __name__ == "__main__":
    main()
