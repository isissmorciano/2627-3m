import csv


def salva_prodotti_csv(prodotti: list[dict], percorso: str) -> None:
    """Scrive una lista di record su un file CSV con intestazione."""
    campi = ["id", "nome", "prezzo", "quantita"]
    with open(percorso, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=campi)
        writer.writeheader()
        writer.writerows(prodotti)


def carica_prodotti_csv(percorso: str) -> list[dict]:
    """Legge un CSV e restituisce i record con i tipi convertiti (int, float)."""
    risultato: list[dict] = []
    try:
        with open(percorso, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for riga in reader:
                risultato.append(
                    {
                        "id": int(riga["id"]),
                        "nome": riga["nome"],
                        "prezzo": float(riga["prezzo"]),
                        "quantita": int(riga["quantita"]),
                    }
                )
    except FileNotFoundError:
        return []
    return risultato


def main() -> None:
    articoli = [
        {"id": 101, "nome": "Tastiera Meccanica", "prezzo": 75.50, "quantita": 12},
        {"id": 102, "nome": "Mouse Wireless", "prezzo": 24.90, "quantita": 30},
    ]

    percorso = "catalogo.csv"
    salva_prodotti_csv(articoli, percorso)
    print(f"Salvati {len(articoli)} articoli in {percorso}")

    caricati = carica_prodotti_csv(percorso)
    for p in caricati:
        print(f"Articolo: {p['nome']} -> Prezzo: {p['prezzo']:.2f}€ (Q.tà: {p['quantita']})")


if __name__ == "__main__":
    main()
