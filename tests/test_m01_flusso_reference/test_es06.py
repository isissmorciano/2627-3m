import pytest

from src.m01_flusso_e_logica_base.es06_reference import main


@pytest.mark.parametrize(
    ("voto", "risultato"),
    [
        ("-1", "Uscita dal programma."),
        ("11", "Errore: voto fuori range."),
        ("4.5", "Giudizio: insufficiente"),
        ("6.5", "Giudizio: sufficiente"),
        ("7.5", "Giudizio: buono"),
        ("8", "Giudizio: ottimo"),
    ],
)
def test_giudizio_e_validazione(monkeypatch, capsys, voto, risultato):
    monkeypatch.setattr("builtins.input", lambda prompt: voto)

    main()

    captured = capsys.readouterr()
    assert risultato in captured.out
