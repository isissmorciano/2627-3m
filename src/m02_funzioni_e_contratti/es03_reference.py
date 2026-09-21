def genera_saluto(nome: str, cognome: str, titolo: str = "Sig./Sig.ra") -> str:
    """Costruisce una formula di benvenuto personalizzata."""
    return f"Benvenuto/a {titolo} {nome} {cognome}!"


def main() -> None:
    saluto1 = genera_saluto("Mario", "Rossi")
    saluto2 = genera_saluto("Laura", "Bianchi", "Dott.ssa")

    print(saluto1)
    print(saluto2)


if __name__ == "__main__":
    main()
