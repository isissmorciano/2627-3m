def main() -> None:
    registro = {
        "Alice": {"Italiano": 8.0, "Matematica": 7.0},
        "Marco": {"Italiano": 6.0, "Matematica": 9.0, "Informatica": 9.0},
        "Sara": {},
    }

    for nome, voti in registro.items():
        if not voti:
            print(f"{nome}: nessun voto")
        else:
            somma = 0.0
            for voto in voti.values():
                somma += voto
            media = somma / len(voti)
            print(f"{nome}: {media:.2f}")


if __name__ == "__main__":
    main()
