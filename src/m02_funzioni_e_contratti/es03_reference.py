def main() -> None:
    rubrica = {"Anna": "123456", "Marco": "654321", "Sara": "111222"}
    nome = input("Nome da cercare: ").strip()

    if nome in rubrica:
        print(f"Numero: {rubrica[nome]}")
    else:
        print("Contatto non trovato.")


if __name__ == "__main__":
    main()
