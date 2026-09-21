def main() -> None:
    while True:
        numero: int = int(input("Inserisci un numero positivo: "))
        if numero > 0:
            print(f"Numero valido: {numero}")
            break
        print("Errore: il numero deve essere positivo.")


if __name__ == "__main__":
    main()
