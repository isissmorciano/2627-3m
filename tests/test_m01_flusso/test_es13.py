from src.m01_flusso_e_logica_base.es13_student import main


def test_input_valido(monkeypatch, capsys):
    inputs = iter(["-5", "0", "12"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Errore: il numero deve essere positivo." in captured.out
    assert "Numero valido: 12" in captured.out
