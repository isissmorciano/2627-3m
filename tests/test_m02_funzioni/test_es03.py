from src.m02_funzioni_e_contratti.es03_student import genera_saluto


def test_saluto_con_titolo_predefinito():
    assert genera_saluto("Mario", "Rossi") == "Benvenuto/a Sig./Sig.ra Mario Rossi!"


def test_saluto_con_titolo_personalizzato():
    assert genera_saluto("Laura", "Bianchi", "Dott.ssa") == "Benvenuto/a Dott.ssa Laura Bianchi!"
