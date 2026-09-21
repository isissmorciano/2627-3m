from src.m01_flusso_e_logica_base.es11_student import main


def test_somma_di_n_numeri(monkeypatch, capsys):
    values = iter(["3", "10", "5", "20"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    assert "La somma totale è: 35" in capsys.readouterr().out


def test_somma_zero_valori(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "0")

    main()

    assert "La somma totale è: 0" in capsys.readouterr().out
