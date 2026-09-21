def componi_tabella_studenti(nomi: list[str], voti: list[float]) -> list[dict]:
    """Combina due liste parallele in una lista di dizionari."""
    if len(nomi) != len(voti):
        return []

    tabella: list[dict] = []
    for i in range(len(nomi)):
        studente = {"nome": nomi[i], "voto": voti[i]}
        tabella.append(studente)

    return tabella


def main() -> None:
    nomi = ["Alice", "Bob", "Carla"]
    voti = [8.5, 7.0, 9.2]

    tabella = componi_tabella_studenti(nomi, voti)
    for riga in tabella:
        print(f"Studente: {riga['nome']} | Voto: {riga['voto']}")


if __name__ == "__main__":
    main()
