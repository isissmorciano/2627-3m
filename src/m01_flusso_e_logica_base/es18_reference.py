def main() -> None:
    numero: int = int(input("Inserisci un intero non negativo: "))

    fattoriale: int = 1
    for fattore in range(1, numero + 1):
        fattoriale *= fattore

    print(f"Il fattoriale di {numero} è: {fattoriale}")


if __name__ == "__main__":
    main()
