from src.m02_funzioni_e_contratti.es05_reference import calcola


def test_operazioni():
    assert calcola(10.0, 2.0, "+") == 12.0
    assert calcola(10.0, 2.0, "-") == 8.0
    assert calcola(10.0, 2.0, "*") == 20.0
    assert calcola(10.0, 2.0, "/") == 5.0


def test_divisione_per_zero():
    assert calcola(10.0, 0.0, "/") is None
