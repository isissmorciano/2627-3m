def main() -> None:
    limite: int = int(input("Inserisci un limite positivo: "))

    conteggio: int = 0
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            conteggio += 1

    print(f"Ci sono {conteggio} numeri pari da 1 a {limite}.")


if __name__ == "__main__":
    main()
