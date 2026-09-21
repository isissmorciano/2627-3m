from src.m03_strutture_dati_e_pattern.es01_reference import rimuovi_negativi


def test_rimuovi_negativi_e_protegge_originale():
    dati_originali = [10, -5, 20, -1, 0]
    copia_sicurezza = dati_originali.copy()

    risultato = rimuovi_negativi(dati_originali)

    assert risultato == [10, 20, 0]
    assert dati_originali == copia_sicurezza
    assert risultato is not dati_originali
