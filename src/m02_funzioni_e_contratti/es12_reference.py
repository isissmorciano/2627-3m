def chiedi_numeri() -> tuple[float, float]:
    """Acquisisce due numeri decimali dall'utente."""
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    return num1, num2


def scegli_operazione() -> str:
    """Mostra le opzioni e restituisce l'operatore scelto."""
    print("\nOperazioni disponibili: +, -, *, /")
    op = input("Scelta: ").strip()
    if op in ["+", "-", "*", "/"]:
        return op
    return ""


def calcola(num1: float, num2: float, operazione: str) -> float | None:
    """Funzione pura: esegue l'operazione aritmetica richiesta."""
    if operazione == "+":
        return num1 + num2
    if operazione == "-":
        return num1 - num2
    if operazione == "*":
        return num1 * num2
    if operazione == "/":
        if num2 == 0:
            return None
        return num1 / num2
    return None


def main() -> None:
    print("Benvenuto nella Calcolatrice Modulare!")
    num1, num2 = chiedi_numeri()
    op = scegli_operazione()

    if not op:
        print("Errore: operazione non riconosciuta.")
        return

    risultato = calcola(num1, num2, op)

    if risultato is None:
        print("Errore: impossibile dividere per zero.")
    else:
        print(f"Il risultato è: {risultato:.2f}")


if __name__ == "__main__":
    main()
