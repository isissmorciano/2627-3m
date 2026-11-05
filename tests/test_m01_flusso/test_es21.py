from src.m01_flusso_e_logica_base.es21_student import main


def verifica_spedizione(monkeypatch, capsys, risposte):
    valori = iter(risposte)
    monkeypatch.setattr("builtins.input", lambda prompt: next(valori))

    main()

    return capsys.readouterr().out


def test_soglia_standard(monkeypatch, capsys):
    output = verifica_spedizione(monkeypatch, capsys, ["50", "n", "n"])

    assert "Spedizione gratuita." in output


def test_soglia_ridotta_per_membri(monkeypatch, capsys):
    output = verifica_spedizione(monkeypatch, capsys, ["30", "s", "n"])

    assert "Spedizione gratuita." in output


def test_soglia_remota(monkeypatch, capsys):
    output = verifica_spedizione(monkeypatch, capsys, ["80", "n", "s"])

    assert "Spedizione gratuita." in output


def test_soglia_non_raggiunta_in_zona_remota(monkeypatch, capsys):
    output = verifica_spedizione(monkeypatch, capsys, ["79.99", "s", "s"])

    assert "Spedizione a pagamento." in output


def test_soglia_membro_non_raggiunta(monkeypatch, capsys):
    output = verifica_spedizione(monkeypatch, capsys, ["29.99", "s", "n"])

    assert "Spedizione a pagamento." in output
