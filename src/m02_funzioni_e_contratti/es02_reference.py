def main() -> None:
    profilo = {"nome": "Alice", "eta": 17}

    eta = int(input("Nuova età: "))
    citta = input("Città: ")
    profilo["eta"] = eta
    profilo["citta"] = citta

    print(f"Nome: {profilo['nome']}")
    print(f"Età: {profilo['eta']}")
    print(f"Città: {profilo['citta']}")


if __name__ == "__main__":
    main()
