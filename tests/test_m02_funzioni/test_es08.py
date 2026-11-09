from src.m02_funzioni_e_contratti.es08_student import calcola_area_triangolo


def test_calcola_area_triangolo():
    assert calcola_area_triangolo(5.0, 3.0) == 7.5
