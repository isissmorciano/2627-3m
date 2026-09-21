from src.m02_funzioni_e_contratti.es06_student import calcola_bmi, classifica_bmi


def test_calcola_bmi():
    # 70 / (1.75 * 1.75) = 22.857...
    assert round(calcola_bmi(70.0, 1.75), 2) == 22.86


def test_classifica_bmi():
    assert classifica_bmi(16.0) == "Sottopeso"
    assert classifica_bmi(22.0) == "Normopeso"
    assert classifica_bmi(27.0) == "Sovrappeso"
    assert classifica_bmi(32.0) == "Obesità"
