def main() -> None:
    frase = input("Frase: ")
    conteggi: dict[str, int] = {}

    for parola in frase.lower().split():
        conteggi[parola] = conteggi.get(parola, 0) + 1

    if not conteggi:
        print("Nessuna parola.")
    else:
        for parola, conteggio in conteggi.items():
            print(f"{parola}: {conteggio}")


if __name__ == "__main__":
    main()
