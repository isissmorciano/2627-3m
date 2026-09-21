from src.m05_file_json_e_package.es01_student import leggi_righe, scrivi_righe


def test_scrivi_e_leggi_righe(tmp_path):
    percorso = tmp_path / "note.txt"
    righe = ["Prima riga", "Seconda riga"]

    scrivi_righe(righe, str(percorso))

    assert leggi_righe(str(percorso)) == righe
