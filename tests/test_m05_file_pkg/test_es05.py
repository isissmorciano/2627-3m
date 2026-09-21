from src.m05_file_json_e_package.quiz import domande, risultati


def test_domande_e_risultati():
    domanda = domande.crea_domanda("2 + 2?", ["3", "4"], 1)
    assert domande.verifica_risposta(domanda, 1) is True

    tabellone = risultati.crea_tabellone()
    risultati.registra_esito(tabellone, True)
    assert risultati.calcola_percentuale(tabellone) == 100.0
