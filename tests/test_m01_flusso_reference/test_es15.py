from src.m01_flusso_e_logica_base.es15_reference import main


def test_conto_alla_rovescia(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "3")

    main()

    output = capsys.readouterr().out
    assert "Conto alla rovescia: 3" in output
    assert "Conto alla rovescia: 0" in output
    assert "Conto alla rovescia: -1" not in output


def test_conto_alla_rovescia_da_zero(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "0")

    main()

    assert capsys.readouterr().out.strip().endswith("Conto alla rovescia: 0")
