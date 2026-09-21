from src.m03_strutture_dati_e_pattern.es09_reference import raggruppa_per_categoria


def test_raggruppa_per_categoria():
    dati = [
        {"id": 1, "categoria": "Libri"},
        {"id": 2, "categoria": "Informatica"},
        {"id": 3, "categoria": "Libri"},
    ]

    assert raggruppa_per_categoria(dati) == {
        "Libri": [dati[0], dati[2]],
        "Informatica": [dati[1]],
    }
