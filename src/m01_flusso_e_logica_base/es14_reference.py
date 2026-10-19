def main() -> None:
    numero: int = int(input("Inserisci un numero intero: "))

    for moltiplicatore in range(1, 11):
        print(f"{numero} x {moltiplicatore} = {numero * moltiplicatore}")


if __name__ == "__main__":
    main()
