from src.m01_flusso_e_logica_base.es05_student import main


def test_sigla_normalizzata(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: " apr ")

    main()

    captured = capsys.readouterr()
    assert "Il mese APR appartiene alla stagione: primavera." in captured.out


def test_sigla_inesistente(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "XYZ")

    main()

    captured = capsys.readouterr()
    assert "Sigla mese inesistente." in captured.out
