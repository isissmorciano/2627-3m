from src.m02_funzioni_e_contratti.es07_student import main


def test_programma_conversioni(monkeypatch, capsys):
    values = iter(["0", "10"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    output = capsys.readouterr().out
    assert "32.0" in output
    assert "6.21" in output
