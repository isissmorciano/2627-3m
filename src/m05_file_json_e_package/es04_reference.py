from .coordinate import linee, punti


def main() -> None:
    punto_a = punti.crea_punto(0.0, 0.0)
    punto_b = punti.crea_punto(3.0, 4.0)
    linea = linee.crea_linea(punto_a, punto_b)
    print(f"Lunghezza: {linee.lunghezza_linea(linea)}")
    print(f"Punto medio: {punti.info_punto(linee.punto_medio(linea))}")


if __name__ == "__main__":
    main()
