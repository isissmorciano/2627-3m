def main() -> None:
    voti = {"Italiano": 8.0, "Matematica": 7.5, "Informatica": 9.0}
    somma = 0.0
    materia_migliore = ""
    voto_migliore = None

    for materia, voto in voti.items():
        somma += voto
        if voto_migliore is None or voto > voto_migliore:
            materia_migliore = materia
            voto_migliore = voto

    media = somma / len(voti)
    print(f"Media: {media:.2f}")
    print(f"Materia con voto più alto: {materia_migliore} ({voto_migliore})")


if __name__ == "__main__":
    main()
