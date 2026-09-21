from src.m02_funzioni_e_contratti.es02_student import calcola_prezzo_scontato


def test_sconto_valido():
    assert calcola_prezzo_scontato(100.0, 20.0) == 80.0
    assert calcola_prezzo_scontato(50.0, 0.0) == 50.0
    assert calcola_prezzo_scontato(80.0, 100.0) == 0.0


def test_sconto_invalido():
    assert calcola_prezzo_scontato(-10.0, 20.0) == -1.0
    assert calcola_prezzo_scontato(100.0, -5.0) == -1.0
    assert calcola_prezzo_scontato(100.0, 105.0) == -1.0
