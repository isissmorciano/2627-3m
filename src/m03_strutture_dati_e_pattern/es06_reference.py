def estrai_nomi_prodotti(prodotti: list[dict]) -> list[str]:
    """Estrae la lista dei soli nomi da una tabella di record."""
    nomi: list[str] = []
    for p in prodotti:
        nomi.append(p["nome"])
    return nomi


def applica_rincaro(prodotti: list[dict], percentuale: float) -> list[dict]:
    """Crea una nuova tabella di prodotti con prezzi maggiorati senza toccare l'originale."""
    nuovo_catalogo: list[dict] = []
    moltiplicatore = 1.0 + (percentuale / 100.0)

    for p in prodotti:
        copia_prodotto = p.copy()
        copia_prodotto["prezzo"] = round(copia_prodotto["prezzo"] * moltiplicatore, 2)
        nuovo_catalogo.append(copia_prodotto)

    return nuovo_catalogo


def main() -> None:
    catalogo = [
        {"id": 101, "nome": "Laptop", "prezzo": 1000.0, "categoria": "Informatica"},
        {"id": 102, "nome": "Tastiera", "prezzo": 50.0, "categoria": "Informatica"},
    ]

    nomi = estrai_nomi_prodotti(catalogo)
    print(f"Elenco nomi: {nomi}")

    prezzi_nuovi = applica_rincaro(catalogo, 20.0)
    print(f"Prezzo originale Laptop: {catalogo[0]['prezzo']}€")
    print(f"Prezzo rincarato Laptop: {prezzi_nuovi[0]['prezzo']}€")


if __name__ == "__main__":
    main()
