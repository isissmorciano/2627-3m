from src.m02_funzioni_e_contratti.es01_reference import main


def test_scheda_studente(capsys):
    main()
    assert capsys.readouterr().out == "Nome: Alice\nEtà: 17\nClasse: 3A\n"
