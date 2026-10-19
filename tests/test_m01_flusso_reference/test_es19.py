from src.m01_flusso_e_logica_base.es19_reference import main


def test_riepilogo_positivi_negativi_e_somma(monkeypatch, capsys):
    values = iter(["4", "-2", "7", "0"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    output = capsys.readouterr().out
    assert "Numeri positivi: 2" in output
    assert "Numeri negativi: 1" in output
    assert "Somma: 9" in output


def test_sentinella_subito(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "0")

    main()

    output = capsys.readouterr().out
    assert "Numeri positivi: 0" in output
    assert "Numeri negativi: 0" in output
    assert "Somma: 0" in output
