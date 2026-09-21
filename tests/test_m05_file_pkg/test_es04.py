from src.m05_file_json_e_package.coordinate import linee, punti


def test_coordinate_linee():
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(3.0, 4.0)
    linea = linee.crea_linea(p1, p2)

    assert linee.lunghezza_linea(linea) == 5.0
    assert linee.punto_medio(linea) == {"x": 1.5, "y": 2.0}
