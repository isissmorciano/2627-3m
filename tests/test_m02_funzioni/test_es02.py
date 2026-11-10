from src.m02_funzioni_e_contratti.es02_reference import main


def test_aggiorna_profilo(monkeypatch, capsys):
    valori = iter(("18", "Lecce"))
    monkeypatch.setattr("builtins.input", lambda prompt: next(valori))
    main()
    assert capsys.readouterr().out == "Nome: Alice\nEtà: 18\nCittà: Lecce\n"
