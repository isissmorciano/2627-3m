from .quiz import domande, risultati


def main() -> None:
    domanda = domande.crea_domanda("Qual è il risultato di 2 + 2?", ["3", "4", "5"], 1)
    tabellone = risultati.crea_tabellone()
    risultati.registra_esito(tabellone, domande.verifica_risposta(domanda, 1))
    print(f"Percentuale: {risultati.calcola_percentuale(tabellone)}%")


if __name__ == "__main__":
    main()
