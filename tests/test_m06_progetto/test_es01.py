from src.m06_pipeline_dati_e_report.es01_student import (
    calcola_fatturato_totale,
    conta_pezzi_per_categoria,
    trova_ordine_top,
)


def test_pipeline_ordini():
    ordini_mock = [
        {"id": 1, "prodotto": "Mouse", "categoria": "Informatica", "quantita": 2, "prezzo_unitario": 20.0},
        {"id": 2, "prodotto": "Libro", "categoria": "Libri", "quantita": 3, "prezzo_unitario": 10.0},
    ]

    assert calcola_fatturato_totale(ordini_mock) == 70.0
    assert conta_pezzi_per_categoria(ordini_mock, "Informatica") == 2
    assert trova_ordine_top(ordini_mock)["prodotto"] == "Mouse"
