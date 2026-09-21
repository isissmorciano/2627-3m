def main() -> None:
    lato1: float = float(input("Inserisci la lunghezza del primo lato: "))
    lato2: float = float(input("Inserisci la lunghezza del secondo lato: "))
    lato3: float = float(input("Inserisci la lunghezza del terzo lato: "))

    ipotenusa: float = max(lato1, lato2, lato3)

    if ipotenusa == lato1:
        somma_quadrati: float = lato2**2 + lato3**2
    elif ipotenusa == lato2:
        somma_quadrati = lato1**2 + lato3**2
    else:
        somma_quadrati = lato1**2 + lato2**2

    if abs(ipotenusa**2 - somma_quadrati) < 1e-6:
        print("Il triangolo è rettangolo.")
    else:
        print("Il triangolo non è rettangolo.")


if __name__ == "__main__":
    main()
