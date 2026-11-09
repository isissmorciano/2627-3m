def main() -> None:
    prezzi = {"Quaderno": 2.5, "Penna": 1.0, "Zaino": 30.0}
    prezzo_massimo = float(input("Prezzo massimo: "))
    trovato = False

    for prodotto, prezzo in prezzi.items():
        if prezzo <= prezzo_massimo:
            print(f"{prodotto}: {prezzo:.2f} euro")
            trovato = True

    if not trovato:
        print("Nessun prodotto trovato.")


if __name__ == "__main__":
    main()
