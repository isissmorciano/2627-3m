from src.m01_flusso_e_logica_base.es03_reference import main


def test_adulto(monkeypatch, capsys):
    inputs = iter(["Mario", "25"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Ciao Mario!" in captured.out
    assert "Sei adulto." in captured.out
