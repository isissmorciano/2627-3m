def calcola_area_triangolo(base: float, altezza: float) -> float:
    """Calcola l'area di un triangolo."""
    return (base * altezza) / 2


def main() -> None:
    base = float(input("Inserisci la base: "))
    altezza = float(input("Inserisci l'altezza: "))

    area = calcola_area_triangolo(base, altezza)

    print(f"Area del triangolo: {area:.2f}")


if __name__ == "__main__":
    main()
