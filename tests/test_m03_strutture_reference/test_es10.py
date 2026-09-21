from src.m03_strutture_dati_e_pattern.es10_reference import crea_indice_per_id


def test_crea_indice_per_id():
    dati = [{"id": 1, "nome": "A"}, {"id": 2, "nome": "B"}]
    indice = crea_indice_per_id(dati)

    assert indice[1] == {"id": 1, "nome": "A"}
    assert indice.get(99) is None


def test_indice_con_lista_vuota():
    assert crea_indice_per_id([]) == {}
