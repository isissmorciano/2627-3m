def main() -> None:
    voto: float = float(input("Inserisci un voto numerico (tra 0 e 10, o negativo per uscire): "))

    if voto < 0:
        print("Uscita dal programma.")
    elif voto > 10:
        print("Errore: voto fuori range.")
    elif voto < 5.0:
        print("Giudizio: insufficiente")
    elif voto <= 6.5:
        print("Giudizio: sufficiente")
    elif voto <= 7.5:
        print("Giudizio: buono")
    else:
        print("Giudizio: ottimo")


if __name__ == "__main__":
    main()
