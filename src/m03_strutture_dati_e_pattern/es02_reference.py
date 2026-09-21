def crea_profilo(nome: str, eta: int, email: str | None = None) -> dict:
    """Costruisce un dizionario profilo utente."""
    profilo: dict = {"nome": nome, "eta": eta}
    if email is not None:
        profilo["email"] = email
    return profilo


def estrai_contatto(profilo: dict) -> str:
    """Restituisce l'email oppure un testo di default se assente."""
    return profilo.get("email", "Nessuna email registrata")


def main() -> None:
    u1 = crea_profilo("Mario", 30, "mario@example.com")
    u2 = crea_profilo("Anna", 22)

    print(f"{u1['nome']} -> {estrai_contatto(u1)}")
    print(f"{u2['nome']} -> {estrai_contatto(u2)}")


if __name__ == "__main__":
    main()
