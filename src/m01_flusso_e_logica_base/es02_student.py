ANNO_CORRENTE: int = 2026


def main() -> None:
    nome_utente: str = input("Inserisci il tuo nome: ")
    anno_nascita: int = int(input("Inserisci il tuo anno di nascita: "))
    eta_utente: int = ANNO_CORRENTE - anno_nascita
    print(f"Ciao {nome_utente}! Quest'anno compi circa {eta_utente} anni.")


if __name__ == "__main__":
    main()
