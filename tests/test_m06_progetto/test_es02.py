from src.m06_pipeline_dati_e_report.es02_student import (
    analizza_prestazioni,
    estrai_squadre_uniche,
    filtra_partite_squadra,
)


def test_pipeline_partite():
    partite = [
        {"casa": "Milan", "trasferta": "Inter", "gol_c": 2, "gol_t": 1},
        {"casa": "Roma", "trasferta": "Milan", "gol_c": 0, "gol_t": 0},
    ]

    assert estrai_squadre_uniche(partite) == ["Inter", "Milan", "Roma"]
    assert len(filtra_partite_squadra(partite, "Milan")) == 2
    assert analizza_prestazioni(partite, "Milan")["v"] == 1
