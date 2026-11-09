def calcola_prezzo_scontato(prezzo: float, percentuale: float) -> float:
    """Calcola il prezzo finale dopo aver applicato lo sconto percentuale."""
    if prezzo < 0 or percentuale < 0 or percentuale > 100:
        return -1.0

    quota_sconto = (prezzo * percentuale) / 100.0
    return prezzo - quota_sconto


def main() -> None:
    prezzo = float(input("Prezzo originale: "))
    perc = float(input("Percentuale di sconto: "))

    risultato = calcola_prezzo_scontato(prezzo, perc)

    if risultato == -1.0:
        print("Errore: dati di input non validi.")
    else:
        print(f"Prezzo scontato: {risultato:.2f}€")


if __name__ == "__main__":
    main()
