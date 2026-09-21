from .biblioteca import catalogo, prestiti


def main() -> None:
    libri = [
        catalogo.crea_libro("Python", "Autore", "Tecnologia", 2),
        catalogo.crea_libro("Romanzo", "Autore", "Narrativa", 1),
    ]
    prestiti.presta_libro(libri[0])
    print(f"Libri tecnologici: {catalogo.filtra_per_genere(libri, 'tecnologia')}")


if __name__ == "__main__":
    main()
