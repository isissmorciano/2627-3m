def rimuovi_negativi(numeri: list[int]) -> list[int]:
    """Restituisce una nuova lista con soli numeri >= 0 senza toccare l'originale."""
    risultato: list[int] = []
    for n in numeri:
        if n >= 0:
            risultato.append(n)
    return risultato


def main() -> None:
    originali: list[int] = [8, -3, 12, -7, 0, 5]
    puliti = rimuovi_negativi(originali)

    print(f"Lista filtrata:   {puliti}")
    print(f"Lista originale:  {originali} (salva da modifiche)")


if __name__ == "__main__":
    main()
