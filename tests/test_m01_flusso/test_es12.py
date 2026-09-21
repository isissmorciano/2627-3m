from src.m01_flusso_e_logica_base.es12_student import main


def test_somma_intervallo_inclusivo(monkeypatch, capsys):
    values = iter(["5", "9"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    assert "La somma dei numeri nell'intervallo [5, 9] è: 35" in capsys.readouterr().out


def test_intervallo_con_un_solo_valore(monkeypatch, capsys):
    values = iter(["-3", "-3"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    assert "La somma dei numeri nell'intervallo [-3, -3] è: -3" in capsys.readouterr().out
