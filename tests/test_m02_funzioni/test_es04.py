import pytest

from src.m02_funzioni_e_contratti.es04_reference import main


@pytest.mark.parametrize(
    ("prezzo", "expected"),
    [
        ("2.5", "Quaderno: 2.50 euro\nPenna: 1.00 euro\n"),
        ("0", "Nessun prodotto trovato.\n"),
        ("30", "Quaderno: 2.50 euro\nPenna: 1.00 euro\nZaino: 30.00 euro\n"),
    ],
)
def test_prezzi(prezzo, expected, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: prezzo)
    main()
    assert capsys.readouterr().out == expected
