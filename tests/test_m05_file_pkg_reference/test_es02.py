from src.m05_file_json_e_package.es02_reference import carica_studenti, salva_studenti


def test_salva_e_carica_json(tmp_path):
    percorso = tmp_path / "archivio.json"
    studenti = [{"nome": "Alice", "media": 8.5}]

    assert salva_studenti(studenti, str(percorso)) is True
    assert carica_studenti(str(percorso)) == studenti


def test_json_assente_o_corrotto(tmp_path):
    percorso = tmp_path / "corrotto.json"
    percorso.write_text("non è json", encoding="utf-8")

    assert carica_studenti(str(percorso)) == []
    assert carica_studenti(str(tmp_path / "assente.json")) == []
