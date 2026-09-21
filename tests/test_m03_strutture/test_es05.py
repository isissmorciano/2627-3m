from src.m03_strutture_dati_e_pattern.es05_student import filtra_per_categoria


PRODOTTI = [
    {"id": 1, "nome": "Libro", "categoria": "Libri"},
    {"id": 2, "nome": "Laptop", "categoria": "Informatica"},
]


def test_filtra_categoria_senza_distinguere_maiuscole():
    assert filtra_per_categoria(PRODOTTI, "libri") == [PRODOTTI[0]]


def test_filtra_categoria_assente():
    assert filtra_per_categoria(PRODOTTI, "Arredamento") == []
