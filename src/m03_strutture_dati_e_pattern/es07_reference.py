def calcola_valore_totale(prodotti: list[dict]) -> float:
    """Calcola la somma complessiva dei prezzi."""
    totale: float = 0.0
    for p in prodotti:
        totale += p["prezzo"]
    return totale


def trova_prodotto_piu_costoso(prodotti: list[dict]) -> dict | None:
    """Individua il prodotto con il prezzo massimo."""
    if not prodotti:
        return None

    migliore = prodotti[0]
    for p in prodotti:
        if p["prezzo"] > migliore["prezzo"]:
            migliore = p

    return migliore


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
        {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    ]

    valore = calcola_valore_totale(catalogo)
    top = trova_prodotto_piu_costoso(catalogo)

    print(f"Valore complessivo: {valore:.2f}€")
    if top:
        print(f"Articolo più caro:  {top['nome']} ({top['prezzo']}€)")


if __name__ == "__main__":
    main()
