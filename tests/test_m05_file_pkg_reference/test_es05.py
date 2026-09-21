from src.m05_file_json_e_package.quiz import domande, risultati


def test_domande():
    domanda = domande.crea_domanda("2 + 2?", ["3", "4"], 1)

    assert domande.verifica_risposta(domanda, 1) is True
    assert domande.verifica_risposta(domanda, 0) is False


def test_risultati_e_json(tmp_path):
    tabellone = risultati.crea_tabellone()
    risultati.registra_esito(tabellone, True)
    risultati.registra_esito(tabellone, False)

    assert risultati.calcola_percentuale(tabellone) == 50.0

    percorso = tmp_path / "risultati.json"
    risultati.salva_risultati(tabellone, str(percorso))
    assert risultati.carica_risultati(str(percorso)) == tabellone
    assert risultati.carica_risultati(str(tmp_path / "assente.json")) == risultati.crea_tabellone()
