import pytest

from src.m02_funzioni_e_contratti.es03_reference import main


@pytest.mark.parametrize(
    ("nome", "expected"),
    [
        (" Marco ", "Numero: 654321\n"),
        ("Luca", "Contatto non trovato.\n"),
        ("marco", "Contatto non trovato.\n"),
    ],
)
def test_rubrica(nome, expected, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: nome)
    main()
    assert capsys.readouterr().out == expected
