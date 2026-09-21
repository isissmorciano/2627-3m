import json

from src.m06_pipeline_dati_e_report.es02_reference import (
    analizza_prestazioni,
    carica_partite,
    estrai_squadre_uniche,
    filtra_partite_squadra,
)


PARTITE = [
    {"data": "2026-01-15", "casa": "Milan", "trasferta": "Juventus", "gol_c": 2, "gol_t": 1},
    {"data": "2026-01-16", "casa": "Juventus", "trasferta": "Milan", "gol_c": 0, "gol_t": 0},
    {"data": "2026-01-17", "casa": "Roma", "trasferta": "Milan", "gol_c": 3, "gol_t": 1},
]


def test_caricamento_e_squadre(tmp_path):
    percorso = tmp_path / "partite.json"
    percorso.write_text(json.dumps(PARTITE), encoding="utf-8")

    caricate = carica_partite(str(percorso))

    assert caricate == PARTITE
    assert estrai_squadre_uniche(caricate) == ["Juventus", "Milan", "Roma"]
    assert len(filtra_partite_squadra(caricate, "Milan")) == 3
    assert carica_partite(str(tmp_path / "assente.json")) == []


def test_analisi_prestazioni():
    statistiche = analizza_prestazioni(PARTITE, "Milan")

    assert statistiche == {
        "squadra": "Milan",
        "partite": 3,
        "v": 1,
        "p": 1,
        "s": 1,
        "gf_media": 1.0,
        "gs_media": 1.33,
        "perc_vittorie": 33.3,
    }
    assert analizza_prestazioni(PARTITE, "Inter")["partite"] == 0
