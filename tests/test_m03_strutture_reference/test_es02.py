from src.m03_strutture_dati_e_pattern.es02_reference import crea_profilo, estrai_contatto


def test_crea_profilo_con_email():
    assert crea_profilo("Mario", 30, "mario@example.com") == {
        "nome": "Mario",
        "eta": 30,
        "email": "mario@example.com",
    }


def test_contatto_senza_email_usa_default():
    profilo = crea_profilo("Anna", 22)

    assert "email" not in profilo
    assert estrai_contatto(profilo) == "Nessuna email registrata"
