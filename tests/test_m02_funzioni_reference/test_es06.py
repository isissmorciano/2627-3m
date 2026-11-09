import pytest

from src.m02_funzioni_e_contratti.es06_reference import main


@pytest.mark.parametrize(
    ("frase", "expected"),
    [
        ("Cane gatto cane", "cane: 2\ngatto: 1\n"),
        ("  ", "Nessuna parola.\n"),
        ("Cane, cane CANE", "cane,: 1\ncane: 2\n"),
    ],
)
def test_conteggio_parole(frase, expected, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: frase)
    main()
    assert capsys.readouterr().out == expected
