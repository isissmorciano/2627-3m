def main() -> None:
    eta: int = int(input("Inserisci la tua età: "))
    ha_tessera: bool = input("Hai una tessera? (s/n): ") == "s"
    corso_completato: bool = input("Hai completato il corso di sicurezza? (s/n): ") == "s"
    ha_autorizzazione: bool = input("Hai un'autorizzazione? (s/n): ") == "s"
    tessera_sospesa: bool = input("La tessera è sospesa? (s/n): ") == "s"

    puo_usare_il_laboratorio: bool = (
        ha_tessera
        and not tessera_sospesa
        and (corso_completato or (eta >= 16 and ha_autorizzazione))
    )

    if puo_usare_il_laboratorio:
        print("Accesso consentito.")
    else:
        print("Accesso negato.")


if __name__ == "__main__":
    main()
