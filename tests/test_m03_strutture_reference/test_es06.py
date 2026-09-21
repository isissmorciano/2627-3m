from src.m03_strutture_dati_e_pattern.es06_reference import applica_rincaro, estrai_nomi_prodotti


PRODOTTI = [
    {"id": 1, "nome": "Libro", "prezzo": 35.0},
    {"id": 2, "nome": "Laptop", "prezzo": 100.0},
]


def test_estrai_nomi_prodotti():
    assert estrai_nomi_prodotti(PRODOTTI) == ["Libro", "Laptop"]


def test_applica_rincaro_non_modifica_originale():
    aumentati = applica_rincaro(PRODOTTI, 10.0)

    assert aumentati[0]["prezzo"] == 38.5
    assert PRODOTTI[0]["prezzo"] == 35.0
    assert aumentati[0] is not PRODOTTI[0]
