import json


# --- 1. STRATO I/O ---
def carica_partite(percorso: str) -> list[dict]:
    """Carica i dati delle partite da file JSON."""
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            dati = json.load(file)
            return dati if isinstance(dati, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# --- 2. STRATO LOGICA PURA ---
def estrai_squadre_uniche(partite: list[dict]) -> list[str]:
    """Restituisce l'elenco delle squadre uniche presenti nel calendario."""
    squadre: list[str] = []
    for partita in partite:
        if partita["casa"] not in squadre:
            squadre.append(partita["casa"])
        if partita["trasferta"] not in squadre:
            squadre.append(partita["trasferta"])
    return sorted(squadre)


def filtra_partite_squadra(partite: list[dict], squadra: str) -> list[dict]:
    """Estrae tutte le partite giocate da una determinata squadra."""
    return [partita for partita in partite if partita["casa"] == squadra or partita["trasferta"] == squadra]


def analizza_prestazioni(partite: list[dict], squadra: str) -> dict:
    """Calcola le metriche complete per una singola squadra."""
    partite_squadra = filtra_partite_squadra(partite, squadra)
    numero_partite = len(partite_squadra)

    if numero_partite == 0:
        return {
            "squadra": squadra,
            "partite": 0,
            "v": 0,
            "p": 0,
            "s": 0,
            "gf_media": 0.0,
            "gs_media": 0.0,
            "perc_vittorie": 0.0,
        }

    vittorie = 0
    pareggi = 0
    sconfitte = 0
    gol_fatti = 0
    gol_subiti = 0

    for partita in partite_squadra:
        squadra_in_casa = partita["casa"] == squadra
        gol_fatti_partita = partita["gol_c"] if squadra_in_casa else partita["gol_t"]
        gol_subiti_partita = partita["gol_t"] if squadra_in_casa else partita["gol_c"]

        gol_fatti += gol_fatti_partita
        gol_subiti += gol_subiti_partita

        if gol_fatti_partita > gol_subiti_partita:
            vittorie += 1
        elif gol_fatti_partita == gol_subiti_partita:
            pareggi += 1
        else:
            sconfitte += 1

    return {
        "squadra": squadra,
        "partite": numero_partite,
        "v": vittorie,
        "p": pareggi,
        "s": sconfitte,
        "gf_media": round(gol_fatti / numero_partite, 2),
        "gs_media": round(gol_subiti / numero_partite, 2),
        "perc_vittorie": round((vittorie / numero_partite) * 100.0, 1),
    }


# --- 3. STRATO PRESENTAZIONE ---
def stampa_tabella_statistiche(statistiche: list[dict]) -> None:
    """Stampa la classifica ordinata per percentuale vittorie."""
    print("\n" + "=" * 75)
    print("                      STATISTICHE CAMPIONATO                      ")
    print("=" * 75)
    print(f"{'Squadra':<15} {'G':<5} {'V-P-S':<10} {'Gol Fatti':<12} {'Gol Subiti':<12} {'% Vittorie'}")
    print("-" * 75)

    statistiche_ordinate = sorted(statistiche, key=lambda statistica: statistica["perc_vittorie"], reverse=True)

    for statistica in statistiche_ordinate:
        record_vps = f"{statistica['v']}-{statistica['p']}-{statistica['s']}"
        print(
            f"{statistica['squadra']:<15} "
            f"{statistica['partite']:<5} "
            f"{record_vps:<10} "
            f"{statistica['gf_media']:<12.2f} "
            f"{statistica['gs_media']:<12.2f} "
            f"{statistica['perc_vittorie']:.1f}%"
        )
    print("=" * 75 + "\n")


# --- 4. ORCHESTRAZIONE ---
def main() -> None:
    partite = carica_partite("partite.json")
    if not partite:
        print("Errore: nessun dato trovato in 'partite.json'.")
        return

    squadre = estrai_squadre_uniche(partite)
    statistiche = [analizza_prestazioni(partite, squadra) for squadra in squadre]

    stampa_tabella_statistiche(statistiche)


if __name__ == "__main__":
    main()
