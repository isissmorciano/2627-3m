def promo_candidato_1(studenti: list[dict]) -> list[str]:
    nomi = []
    for s in studenti:
        if s["voto"] < 6.0:
            studenti.remove(s)
        else:
            nomi.append(s["nome"])
    return nomi


def promo_candidato_2(studenti: list[dict]) -> list[str]:
    nomi = []
    for s in studenti:
        if s["voto"] > 6.0:
            nomi.append(s["nome"])
    return nomi


def promo_candidato_3(studenti: list[dict]) -> list[str]:
    promossi: list[str] = []
    for s in studenti:
        if s.get("voto", 0.0) >= 6.0:
            promossi.append(s["nome"])
    return promossi


def test_inclusione_sufficienza_esatta():
    dati = [{"nome": "Marco", "voto": 6.0}, {"nome": "Anna", "voto": 5.5}]

    assert promo_candidato_3(dati) == ["Marco"]


def test_rispetto_dati_originali():
    dati_originali = [{"nome": "Luca", "voto": 4.0}, {"nome": "Sara", "voto": 8.0}]
    copia_controllo = [s.copy() for s in dati_originali]

    promo_candidato_3(dati_originali)

    assert dati_originali == copia_controllo
