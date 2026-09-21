from .funzioni_sconto import calcola_prezzo_scontato


def test_sconto_normale():
    assert calcola_prezzo_scontato(100.0, 20.0) == 80.0


def test_sconto_zero():
    assert calcola_prezzo_scontato(50.0, 0.0) == 50.0


def test_sconto_totale():
    assert calcola_prezzo_scontato(75.0, 100.0) == 0.0


def test_dati_non_validi():
    assert calcola_prezzo_scontato(-10.0, 20.0) == -1.0
    assert calcola_prezzo_scontato(100.0, 150.0) == -1.0
