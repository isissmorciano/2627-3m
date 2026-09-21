from src.m03_strutture_dati_e_pattern.es07_student import (
    calcola_valore_totale,
    trova_prodotto_piu_costoso,
)


PRODOTTI = [
    {"id": 1, "nome": "Libro", "prezzo": 35.0},
    {"id": 2, "nome": "Laptop", "prezzo": 100.0},
]


def test_calcola_valore_totale():
    assert calcola_valore_totale(PRODOTTI) == 135.0
    assert calcola_valore_totale([]) == 0.0


def test_trova_prodotto_piu_costoso():
    assert trova_prodotto_piu_costoso(PRODOTTI) == PRODOTTI[1]
    assert trova_prodotto_piu_costoso([]) is None
