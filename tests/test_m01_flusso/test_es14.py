from src.m01_flusso_e_logica_base.es14_student import main


def test_tabellina_con_for(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "7")

    main()

    output = capsys.readouterr().out
    assert "7 x 1 = 7" in output
    assert "7 x 5 = 35" in output
    assert "7 x 10 = 70" in output
