from src.m01_flusso_e_logica_base.es18_reference import main


def test_fattoriale_con_for(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "5")

    main()

    assert "Il fattoriale di 5 è: 120" in capsys.readouterr().out


def test_fattoriale_di_zero(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "0")

    main()

    assert "Il fattoriale di 0 è: 1" in capsys.readouterr().out
