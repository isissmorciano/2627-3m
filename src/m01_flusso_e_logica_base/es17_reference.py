def main() -> None:
    somma: int = 0
    numero: int = int(input("Inserisci un numero (0 per terminare): "))

    while numero != 0:
        somma += numero
        numero = int(input("Inserisci un numero (0 per terminare): "))

    print(f"La somma totale è: {somma}")


if __name__ == "__main__":
    main()
