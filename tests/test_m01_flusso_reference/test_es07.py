from src.m01_flusso_e_logica_base.es07_reference import main


def run_equazione(monkeypatch, inputs):
    values = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))
    main()


def test_soluzione_unica(monkeypatch, capsys):
    run_equazione(monkeypatch, ["2", "4"])

    assert "La soluzione è x = -2.0" in capsys.readouterr().out


def test_equazione_indeterminata(monkeypatch, capsys):
    run_equazione(monkeypatch, ["0", "0"])

    assert "L'equazione è indeterminata (infinite soluzioni)." in capsys.readouterr().out


def test_equazione_impossibile(monkeypatch, capsys):
    run_equazione(monkeypatch, ["0", "4"])

    assert "L'equazione è impossibile (nessuna soluzione)." in capsys.readouterr().out
