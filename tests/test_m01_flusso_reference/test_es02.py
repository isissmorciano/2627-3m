from src.m01_flusso_e_logica_base.es02_reference import main


def test_eta_calcolo(monkeypatch, capsys):
    inputs = iter(["Anna", "1990"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Anna! Quest'anno compi circa 36 anni." in captured.out
