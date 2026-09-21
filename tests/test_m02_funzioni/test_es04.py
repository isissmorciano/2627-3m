from src.m02_funzioni_e_contratti.es04_student import calcola_rettangolo


def test_calcola_rettangolo():
    area, perimetro = calcola_rettangolo(5.0, 3.0)
    assert area == 15.0
    assert perimetro == 16.0
