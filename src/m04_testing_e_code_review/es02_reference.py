from .es02_corretta import valuta_voto


def test_giudizio_tipico():
    assert valuta_voto(7.0) == "Sufficiente"
    assert valuta_voto(4.5) == "Insufficiente"
    assert valuta_voto(9.0) == "Ottimo"


def test_soglie_di_confine_esatte():
    assert valuta_voto(8.0) == "Ottimo"
    assert valuta_voto(6.0) == "Sufficiente"
    assert valuta_voto(0.0) == "Insufficiente"
    assert valuta_voto(10.0) == "Ottimo"


def test_valori_fuori_scala():
    assert valuta_voto(-0.5) == "Non Valido"
    assert valuta_voto(10.5) == "Non Valido"
