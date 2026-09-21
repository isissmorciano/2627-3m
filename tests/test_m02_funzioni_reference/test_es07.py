from src.m02_funzioni_e_contratti.conversioni import celsius_a_fahrenheit, km_a_miglia
from src.m02_funzioni_e_contratti.es07_reference import main


def test_conversione_celsius_fahrenheit():
    assert celsius_a_fahrenheit(0.0) == 32.0
    assert celsius_a_fahrenheit(100.0) == 212.0


def test_conversione_km_miglia():
    assert km_a_miglia(10.0) == 6.21371


def test_programma_conversioni(monkeypatch, capsys):
    values = iter(["0", "10"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    output = capsys.readouterr().out
    assert "32.0" in output
    assert "6.21" in output
