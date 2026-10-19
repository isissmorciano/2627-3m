from src.m01_flusso_e_logica_base.es17_reference import main


def test_somma_fino_al_sentinella(monkeypatch, capsys):
    values = iter(["4", "-2", "0"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    assert "La somma totale è: 2" in capsys.readouterr().out


def test_sentinella_subito(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "0")

    main()

    assert "La somma totale è: 0" in capsys.readouterr().out
