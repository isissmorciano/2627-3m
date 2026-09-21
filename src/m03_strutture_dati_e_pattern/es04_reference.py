def trova_prodotto_per_id(prodotti: list[dict], id_cercato: int) -> dict | None:
    """Restituisce il prodotto cercato oppure None se non presente."""
    for p in prodotti:
        if p["id"] == id_cercato:
            return p
    return None


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
        {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    ]

    trovato = trova_prodotto_per_id(catalogo, 102)
    if trovato:
        print(f"Trovato: {trovato['nome']} ({trovato['prezzo']}€)")
    else:
        print("Articolo non trovato.")


if __name__ == "__main__":
    main()
