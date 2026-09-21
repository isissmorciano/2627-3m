def scrivi_righe(righe: list[str], percorso: str) -> None:
    """Scrive un elenco di stringhe su file di testo, una per riga."""
    with open(percorso, "w", encoding="utf-8") as file:
        for riga in righe:
            file.write(f"{riga}\n")


def leggi_righe(percorso: str) -> list[str]:
    """Legge le righe da file. Restituisce [] se il file non esiste."""
    risultato: list[str] = []
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            for riga in file:
                risultato.append(riga.strip())
    except FileNotFoundError:
        return []
    return risultato


def main() -> None:
    dati = ["Prima nota", "Seconda nota", "Terza nota"]
    percorso = "note.txt"

    scrivi_righe(dati, percorso)
    print("File scritto.")

    lette = leggi_righe(percorso)
    print(f"Righe lette: {lette}")

    fantasma = leggi_righe("non_esiste.txt")
    print(f"Lettura file inesistente: {fantasma}")


if __name__ == "__main__":
    main()
