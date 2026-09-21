from src.m06_pipeline_dati_e_report.es01_reference import (
    carica_ordini,
    calcola_fatturato_totale,
    conta_pezzi_per_categoria,
    trova_ordine_top,
)


def test_pipeline_ordini(tmp_path):
    percorso = tmp_path / "ordini.csv"
    percorso.write_text(
        "id_ordine,prodotto,categoria,quantita,prezzo_unitario\n1,Mouse,Informatica,2,20.0\n2,Libro,Libri,3,10.0\n",
        encoding="utf-8",
    )

    ordini = carica_ordini(str(percorso))

    assert ordini[0]["id"] == 1
    assert ordini[0]["quantita"] == 2
    assert ordini[0]["prezzo_unitario"] == 20.0
    assert calcola_fatturato_totale(ordini) == 70.0
    assert conta_pezzi_per_categoria(ordini, "informatica") == 2
    assert trova_ordine_top(ordini)["prodotto"] == "Mouse"
    assert carica_ordini(str(tmp_path / "assente.csv")) == []


def test_ordine_top_su_lista_vuota():
    assert trova_ordine_top([]) is None
