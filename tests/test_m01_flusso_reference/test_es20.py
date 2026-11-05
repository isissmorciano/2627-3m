from src.m01_flusso_e_logica_base.es20_reference import main


def esegui_main(monkeypatch, capsys, risposte):
    valori = iter(risposte)
    monkeypatch.setattr("builtins.input", lambda prompt: next(valori))

    main()

    return capsys.readouterr().out


def test_accesso_con_eta_e_autorizzazione(monkeypatch, capsys):
    output = esegui_main(monkeypatch, capsys, ["16", "s", "n", "s", "n"])

    assert "Accesso consentito." in output


def test_accesso_con_corso_completato(monkeypatch, capsys):
    output = esegui_main(monkeypatch, capsys, ["13", "s", "s", "n", "n"])

    assert "Accesso consentito." in output


def test_accesso_negato_se_manca_requisito(monkeypatch, capsys):
    output = esegui_main(monkeypatch, capsys, ["16", "s", "n", "n", "n"])

    assert "Accesso negato." in output


def test_accesso_negato_con_tessera_sospesa(monkeypatch, capsys):
    output = esegui_main(monkeypatch, capsys, ["18", "s", "s", "s", "s"])

    assert "Accesso negato." in output
