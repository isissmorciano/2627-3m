from src.m05_file_json_e_package.biblioteca import catalogo, prestiti


def test_catalogo_e_prestiti():
    libro = catalogo.crea_libro("Python", "Autore", "Tecnologia", 1)

    assert prestiti.presta_libro(libro) is True
    assert libro["copie"] == 0
