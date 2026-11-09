def calcola_rettangolo(base: float, altezza: float) -> tuple[float, float]:
    """Calcola area e perimetro di un rettangolo."""
    area = base * altezza
    perimetro = 2 * (base + altezza)
    return area, perimetro


def main() -> None:
    base = float(input("Inserisci la base: "))
    altezza = float(input("Inserisci l'altezza: "))

    area, perimetro = calcola_rettangolo(base, altezza)

    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")


if __name__ == "__main__":
    main()
