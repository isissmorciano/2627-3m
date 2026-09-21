import math


def crea_punto(x: float, y: float) -> dict:
    return {"x": x, "y": y}


def distanza_tra_punti(p1: dict, p2: dict) -> float:
    dx = p2["x"] - p1["x"]
    dy = p2["y"] - p1["y"]
    return math.sqrt(dx**2 + dy**2)


def info_punto(punto: dict) -> str:
    return f"({punto['x']}, {punto['y']})"
