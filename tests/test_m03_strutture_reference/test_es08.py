from src.m03_strutture_dati_e_pattern.es08_reference import conta_frequenze_categorie


def test_frequenze():
    dati = [
        {"categoria": "Libri"},
        {"categoria": "Informatica"},
        {"categoria": "Libri"},
    ]

    assert conta_frequenze_categorie(dati) == {"Libri": 2, "Informatica": 1}
