from src.m05_file_json_e_package.es03_student import carica_prodotti_csv, salva_prodotti_csv


def test_salva_e_carica_csv(tmp_path):
    percorso = tmp_path / "prodotti.csv"
    prodotti = [{"id": 101, "nome": "Tastiera", "prezzo": 75.5, "quantita": 10}]

    salva_prodotti_csv(prodotti, str(percorso))

    assert carica_prodotti_csv(str(percorso)) == prodotti
