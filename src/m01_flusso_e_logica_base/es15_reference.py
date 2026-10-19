def main() -> None:
    numero: int = int(input("Inserisci un numero non negativo: "))

    while numero >= 0:
        print(f"Conto alla rovescia: {numero}")
        numero -= 1


if __name__ == "__main__":
    main()
