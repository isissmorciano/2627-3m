from src.m03_strutture_dati_e_pattern.es04_student import trova_prodotto_per_id


PRODOTTI = [{"id": 1, "nome": "A"}, {"id": 2, "nome": "B"}]


def test_trova_prodotto_esistente():
    assert trova_prodotto_per_id(PRODOTTI, 2) == {"id": 2, "nome": "B"}


def test_trova_prodotto_inesistente():
    assert trova_prodotto_per_id(PRODOTTI, 99) is None
