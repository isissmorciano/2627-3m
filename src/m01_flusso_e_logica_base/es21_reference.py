def main() -> None:
    totale: float = float(input("Totale dell'ordine in euro: "))
    membro_del_club: bool = input("Sei membro del club? (s/n): ") == "s"
    zona_remota: bool = input("Abiti in una zona remota? (s/n): ") == "s"

    soglia_raggiunta: bool = totale >= 50 or (membro_del_club and totale >= 30)
    spedizione_gratuita: bool = soglia_raggiunta and (not zona_remota or totale >= 80)

    if spedizione_gratuita:
        print("Spedizione gratuita.")
    else:
        print("Spedizione a pagamento.")


if __name__ == "__main__":
    main()
