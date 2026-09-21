import pytest

from src.m01_flusso_e_logica_base.es10_reference import main


@pytest.mark.parametrize(
    "lati",
    [["3", "4", "5"], ["5", "3", "4"], ["3", "5", "4"]],
)
def test_triangolo_rettangolo_con_qualsiasi_ipotenusa(monkeypatch, capsys, lati):
    values = iter(lati)
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    assert "Il triangolo è rettangolo." in capsys.readouterr().out


def test_triangolo_non_rettangolo(monkeypatch, capsys):
    values = iter(["2", "3", "4"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))

    main()

    assert "Il triangolo non è rettangolo." in capsys.readouterr().out
