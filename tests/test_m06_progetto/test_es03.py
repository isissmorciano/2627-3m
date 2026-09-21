from src.m06_pipeline_dati_e_report.es03_student import (
    calcola_statistiche,
    cerca_per_nome,
    valida_voto,
)


def test_valida_voto():
    assert valida_voto("8.5")[0] is True
    assert valida_voto("-1")[0] is False
    assert valida_voto("11")[0] is False
    assert valida_voto("abc")[0] is False


def test_cerca_per_nome_substring():
    studenti = [
        {"nome": "Alice Rossi", "voto": 8.0},
        {"nome": "Marco Bianchi", "voto": 6.5},
    ]
    risultati = cerca_per_nome(studenti, "rossi")
    assert len(risultati) == 1
    assert risultati[0]["nome"] == "Alice Rossi"
    assert calcola_statistiche([])["totale"] == 0
