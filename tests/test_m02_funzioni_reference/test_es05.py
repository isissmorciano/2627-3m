from src.m02_funzioni_e_contratti.es05_reference import main


def test_voti(capsys):
    main()
    assert capsys.readouterr().out == (
        "Media: 8.17\nMateria con voto più alto: Informatica (9.0)\n"
    )
