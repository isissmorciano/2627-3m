from src.m01_flusso_e_logica_base.es22_student import main


def verifica_idoneita(monkeypatch, capsys, risposte):
    valori = iter(risposte)
    monkeypatch.setattr("builtins.input", lambda prompt: next(valori))

    main()

    return capsys.readouterr().out


def test_reddito_basso_e_media_minima(monkeypatch, capsys):
    output = verifica_idoneita(monkeypatch, capsys, ["8", "20000", "s", "n"])

    assert "Studente idoneo." in output


def test_reddito_piu_alto_e_media_alta(monkeypatch, capsys):
    output = verifica_idoneita(monkeypatch, capsys, ["9", "30000", "s", "n"])

    assert "Studente idoneo." in output


def test_reddito_alto_e_media_insufficiente(monkeypatch, capsys):
    output = verifica_idoneita(monkeypatch, capsys, ["8.5", "25000", "s", "n"])

    assert "Studente non idoneo." in output


def test_non_residente_non_idoneo(monkeypatch, capsys):
    output = verifica_idoneita(monkeypatch, capsys, ["9", "20000", "n", "n"])

    assert "Studente non idoneo." in output


def test_sanzione_esclude_idoneita(monkeypatch, capsys):
    output = verifica_idoneita(monkeypatch, capsys, ["9", "20000", "s", "s"])

    assert "Studente non idoneo." in output
