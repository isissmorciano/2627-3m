import csv


# --- 1. STRATO I/O ---
def carica_ordini(percorso_file: str) -> list[dict]:
    """Carica gli ordini da file CSV convertendo i tipi numerici."""
    ordini: list[dict] = []
    try:
        with open(percorso_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for riga in reader:
                ordini.append(
                    {
                        "id": int(riga["id_ordine"]),
                        "prodotto": riga["prodotto"],
                        "categoria": riga["categoria"],
                        "quantita": int(riga["quantita"]),
                        "prezzo_unitario": float(riga["prezzo_unitario"]),
                    }
                )
    except FileNotFoundError:
        return []
    return ordini


# --- 2. STRATO LOGICA PURA ---
def calcola_fatturato_totale(ordini: list[dict]) -> float:
    """Aggregazione: calcola l'incasso complessivo di tutti gli ordini."""
    totale = 0.0
    for ordine in ordini:
        totale += ordine["quantita"] * ordine["prezzo_unitario"]
    return totale


def conta_pezzi_per_categoria(ordini: list[dict], categoria: str) -> int:
    """Filtraggio + Aggregazione: somma i pezzi di una categoria."""
    pezzi = 0
    categoria_target = categoria.lower()
    for ordine in ordini:
        if ordine["categoria"].lower() == categoria_target:
            pezzi += ordine["quantita"]
    return pezzi


def trova_ordine_top(ordini: list[dict]) -> dict | None:
    """Ricerca del massimo: trova l'ordine con il ricavo maggiore."""
    if not ordini:
        return None

    migliore = ordini[0]
    ricavo_max = migliore["quantita"] * migliore["prezzo_unitario"]

    for ordine in ordini:
        ricavo_attuale = ordine["quantita"] * ordine["prezzo_unitario"]
        if ricavo_attuale > ricavo_max:
            ricavo_max = ricavo_attuale
            migliore = ordine

    return migliore


# --- 3. STRATO PRESENTAZIONE ---
def stampa_report(fatturato: float, pezzi_libri: int, top_ordine: dict | None) -> None:
    """Stampa il report commerciale formattato a terminale."""
    print("\n==========================================")
    print("       REPORT COMMERCIALE VENDITE         ")
    print("==========================================")
    print(f"Fatturato Complessivo:       {fatturato:.2f}€")
    print(f"Totale Libri Venduti:        {pezzi_libri} copie")

    if top_ordine:
        ricavo = top_ordine["quantita"] * top_ordine["prezzo_unitario"]
        print(f"Miglior Ordine:              '{top_ordine['prodotto']}' ({ricavo:.2f}€)")
    else:
        print("Miglior Ordine:              Nessun dato disponibile")
    print("==========================================\n")


# --- 4. ORCHESTRAZIONE ---
def main() -> None:
    file_dati = "ordini.csv"
    ordini = carica_ordini(file_dati)

    if not ordini:
        print(f"Errore: impossibile caricare i dati da '{file_dati}'.")
        return

    fatturato = calcola_fatturato_totale(ordini)
    libri_venduti = conta_pezzi_per_categoria(ordini, "Libri")
    miglior_ordine = trova_ordine_top(ordini)

    stampa_report(fatturato, libri_venduti, miglior_ordine)


if __name__ == "__main__":
    main()
