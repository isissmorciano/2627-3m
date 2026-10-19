from src.m01_flusso_e_logica_base.es16_reference import main


def test_conteggio_dei_numeri_pari(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "10")

    main()

    assert "Ci sono 5 numeri pari da 1 a 10." in capsys.readouterr().out


def test_limite_senza_numeri_pari(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "1")

    main()

    assert "Ci sono 0 numeri pari da 1 a 1." in capsys.readouterr().out
