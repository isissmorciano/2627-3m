from src.m03_strutture_dati_e_pattern.es03_reference import componi_tabella_studenti


def test_compone_tabella_studenti():
    assert componi_tabella_studenti(["Alice", "Bob"], [8.5, 7.0]) == [
        {"nome": "Alice", "voto": 8.5},
        {"nome": "Bob", "voto": 7.0},
    ]


def test_liste_di_lunghezza_diversa():
    assert componi_tabella_studenti(["Alice"], [8.5, 7.0]) == []
