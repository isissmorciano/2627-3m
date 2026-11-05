def main() -> None:
    media: float = float(input("Inserisci la media scolastica: "))
    reddito_familiare: int = int(input("Inserisci il reddito familiare: "))
    residente: bool = input("Sei residente nella regione? (s/n): ") == "s"
    ha_sanzioni: bool = input("Hai sanzioni disciplinari? (s/n): ") == "s"

    requisiti_economici: bool = reddito_familiare <= 20000 or (
        media >= 9 and reddito_familiare <= 30000
    )
    idoneo: bool = (
        residente and not ha_sanzioni and media >= 8 and requisiti_economici
    )

    if idoneo:
        print("Studente idoneo.")
    else:
        print("Studente non idoneo.")


if __name__ == "__main__":
    main()
