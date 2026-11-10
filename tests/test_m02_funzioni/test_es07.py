from src.m02_funzioni_e_contratti.es07_reference import main


def test_registro_classe(capsys):
    main()
    assert capsys.readouterr().out == "Alice: 7.50\nMarco: 8.00\nSara: nessun voto\n"
