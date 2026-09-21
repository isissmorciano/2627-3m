from src.m01_flusso_e_logica_base.es09_reference import main


def run_equazione(monkeypatch, inputs):
    values = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))
    main()


def test_due_soluzioni_reali(monkeypatch, capsys):
    run_equazione(monkeypatch, ["1", "0", "-4"])

    assert "Le soluzioni sono x1 = 2.0 e x2 = -2.0" in capsys.readouterr().out


def test_soluzione_doppia(monkeypatch, capsys):
    run_equazione(monkeypatch, ["1", "2", "1"])

    assert "La soluzione doppia è x = -1.0" in capsys.readouterr().out


def test_nessuna_soluzione_reale(monkeypatch, capsys):
    run_equazione(monkeypatch, ["1", "0", "1"])

    assert "Non ci sono soluzioni reali." in capsys.readouterr().out
