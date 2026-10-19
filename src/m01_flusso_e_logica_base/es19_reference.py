def main() -> None:
    positivi: int = 0
    negativi: int = 0
    somma: int = 0
    numero: int = int(input("Inserisci un numero (0 per terminare): "))

    while numero != 0:
        if numero > 0:
            positivi += 1
        else:
            negativi += 1
        somma += numero
        numero = int(input("Inserisci un numero (0 per terminare): "))

    print(f"Numeri positivi: {positivi}")
    print(f"Numeri negativi: {negativi}")
    print(f"Somma: {somma}")


if __name__ == "__main__":
    main()
