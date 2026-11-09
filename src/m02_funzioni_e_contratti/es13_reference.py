# --- 1. STRATO LOGICA PURA (Il Cervello) ---
def calcola_bmi(peso: float, altezza: float) -> float:
    """Calcola il valore numerico del BMI."""
    return peso / (altezza**2)


def classifica_bmi(bmi: float) -> str:
    """Restituisce la categoria qualitativa associata al BMI."""
    if bmi < 18.5:
        return "Sottopeso"
    if bmi < 25.0:
        return "Normopeso"
    if bmi < 30.0:
        return "Sovrappeso"
    return "Obesità"


# --- 2. STRATO I/O (Input con validazione) ---
def chiedi_peso() -> float:
    """Chiede il peso e ripete finché non è positivo."""
    while True:
        peso = float(input("Inserisci il peso in kg: "))
        if peso > 0:
            return peso
        print("Errore: il peso deve essere maggiore di zero.")


def chiedi_altezza() -> float:
    """Chiede l'altezza e ripete finché non è positiva."""
    while True:
        altezza = float(input("Inserisci l'altezza in metri: "))
        if altezza > 0:
            return altezza
        print("Errore: l'altezza deve essere maggiore di zero.")


# --- 3. STRATO PRESENTAZIONE (La Voce) ---
def stampa_report_bmi(peso: float, altezza: float, bmi: float, categoria: str) -> None:
    """Stampa la scheda riassuntiva formattata."""
    print("\n=== SCHEDA DI VALUTAZIONE BMI ===")
    print(f"Peso inserito:    {peso:.1f} kg")
    print(f"Altezza inserita: {altezza:.2f} m")
    print(f"Valore BMI:       {bmi:.2f}")
    print(f"Classificazione:  {categoria}")
    print("=================================\n")


# --- 4. ORCHESTRAZIONE (main) ---
def main() -> None:
    peso = chiedi_peso()
    altezza = chiedi_altezza()

    bmi = calcola_bmi(peso, altezza)
    categoria = classifica_bmi(bmi)

    stampa_report_bmi(peso, altezza, bmi, categoria)


if __name__ == "__main__":
    main()
