from src.m05_file_json_e_package.biblioteca import catalogo, prestiti


def test_catalogo_e_prestiti():
    libro = catalogo.crea_libro("Python", "Autore", "Tecnologia", 1)

    assert catalogo.libro_disponibile(libro) is True
    assert prestiti.presta_libro(libro) is True
    assert libro["copie"] == 0
    assert prestiti.presta_libro(libro) is False
    assert prestiti.restituisci_libro(libro) is True
    assert prestiti.restituisci_libro(libro) is False


def test_filtra_e_archivio_json(tmp_path):
    libri = [
        catalogo.crea_libro("Python", "Autore", "Tecnologia", 2),
        catalogo.crea_libro("Romanzo", "Autore", "Narrativa", 1),
    ]

    assert catalogo.filtra_per_genere(libri, "tecnologia") == [libri[0]]

    percorso = tmp_path / "biblioteca.json"
    prestiti.salva_archivio(libri, str(percorso))
    assert prestiti.carica_archivio(str(percorso)) == libri
    assert prestiti.carica_archivio(str(tmp_path / "assente.json")) == []
