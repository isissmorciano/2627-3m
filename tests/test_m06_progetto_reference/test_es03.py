from src.m06_pipeline_dati_e_report.es03_reference import (
    carica_studenti,
    calcola_statistiche,
    cerca_per_nome,
    filtra_per_voti,
    formatta_tabella,
    salva_studenti,
    valida_voto,
)


def test_valida_voto():
    assert valida_voto("8.5") == (True, 8.5)
    assert valida_voto("-1")[0] is False
    assert valida_voto("11")[0] is False
    assert valida_voto("abc")[0] is False


def test_funzioni_pure():
    studenti = [
        {"nome": "Alice Rossi", "voto": 8.0},
        {"nome": "Marco Bianchi", "voto": 6.5},
    ]

    assert cerca_per_nome(studenti, "rossi") == [studenti[0]]
    assert filtra_per_voti(studenti, 7.0, 9.0) == [studenti[0]]
    assert filtra_per_voti(studenti, 9.0, 7.0) == []
    assert calcola_statistiche(studenti) == {
        "totale": 2,
        "media": 7.25,
        "migliore": studenti[0],
        "peggiore": studenti[1],
    }
    assert formatta_tabella([]) == "Nessuno studente presente in archivio."


def test_persistenza_studenti(tmp_path):
    percorso = tmp_path / "studenti.json"
    studenti = [{"nome": "Alice", "voto": 8.5}]

    assert salva_studenti(studenti, str(percorso)) is True
    assert carica_studenti(str(percorso)) == studenti
    assert carica_studenti(str(tmp_path / "assente.json")) == []

    percorso.write_text("contenuto non valido", encoding="utf-8")
    assert carica_studenti(str(percorso)) == []
