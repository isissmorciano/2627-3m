from src.m01_flusso_e_logica_base.es08_reference import main


def test_bisestile_normale(monkeypatch, capsys):
    inputs = iter(["2024"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "L'anno 2024 è bisestile." in captured.out


def test_secolo_non_bisestile(monkeypatch, capsys):
    inputs = iter(["1900"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "L'anno 1900 non è bisestile." in captured.out
