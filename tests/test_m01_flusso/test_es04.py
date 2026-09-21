import pytest

from src.m01_flusso_e_logica_base.es04_student import main


@pytest.mark.parametrize(
    ("eccesso", "multa"),
    [("10", 36), ("25", 148), ("50", 370), ("61", 500)],
)
def test_sanzione_per_scaglione(monkeypatch, capsys, eccesso, multa):
    monkeypatch.setattr("builtins.input", lambda prompt: eccesso)

    main()

    captured = capsys.readouterr()
    assert f"La sanzione amministrativa è di euro {multa}." in captured.out
