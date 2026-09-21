from .punti import crea_punto, distanza_tra_punti, info_punto


def crea_linea(p1: dict, p2: dict) -> dict:
    return {"p1": p1, "p2": p2}


def lunghezza_linea(linea: dict) -> float:
    return distanza_tra_punti(linea["p1"], linea["p2"])


def punto_medio(linea: dict) -> dict:
    xm = (linea["p1"]["x"] + linea["p2"]["x"]) / 2.0
    ym = (linea["p1"]["y"] + linea["p2"]["y"]) / 2.0
    return crea_punto(xm, ym)


def info_linea(linea: dict) -> str:
    return f"Linea da {info_punto(linea['p1'])} a {info_punto(linea['p2'])}"
