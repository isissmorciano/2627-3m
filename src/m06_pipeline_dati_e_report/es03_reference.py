import json
import os

STORAGE_FILE = "studenti.json"


# --- STRATO 1: PERSISTENZA E VALIDAZIONE ---
def carica_studenti(percorso: str = STORAGE_FILE) -> list[dict]:
    """Carica gli studenti da file JSON."""
    if not os.path.exists(percorso):
        return []
    try:
        with open(percorso, "r", encoding="utf-8") as file:
            dati = json.load(file)
            return dati if isinstance(dati, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def salva_studenti(studenti: list[dict], percorso: str = STORAGE_FILE) -> bool:
    """Salva la lista di studenti su JSON."""
    try:
        with open(percorso, "w", encoding="utf-8") as file:
            json.dump(studenti, file, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False


def valida_voto(voto_str: str) -> tuple[bool, float | str]:
    """Valida se una stringa rappresenta un voto numerico valido tra 0 e 10."""
    try:
        voto = float(voto_str)
        if 0.0 <= voto <= 10.0:
            return True, voto
        return False, "Il voto deve essere compreso tra 0.0 e 10.0."
    except ValueError:
        return False, "Inserisci un valore numerico decimale valido."


# --- STRATO 2: LOGICA PURA ---
def cerca_per_nome(studenti: list[dict], termine: str) -> list[dict]:
    """Filtra gli studenti il cui nome contiene il termine di ricerca."""
    termine_pulito = termine.strip().lower()
    if not termine_pulito:
        return []
    return [studente for studente in studenti if termine_pulito in studente["nome"].lower()]


def filtra_per_voti(studenti: list[dict], min_voto: float, max_voto: float) -> list[dict]:
    """Estrae gli studenti che rientrano nella fascia di voto specificata."""
    if min_voto > max_voto:
        return []
    return [studente for studente in studenti if min_voto <= studente["voto"] <= max_voto]


def calcola_statistiche(studenti: list[dict]) -> dict:
    """Calcola metriche di sintesi: totale, media, migliore e peggiore."""
    if not studenti:
        return {"totale": 0, "media": 0.0, "migliore": None, "peggiore": None}

    somma = sum(studente["voto"] for studente in studenti)
    media = round(somma / len(studenti), 2)
    migliore = max(studenti, key=lambda studente: studente["voto"])
    peggiore = min(studenti, key=lambda studente: studente["voto"])

    return {
        "totale": len(studenti),
        "media": media,
        "migliore": migliore,
        "peggiore": peggiore,
    }


# --- STRATO 3: PRESENTAZIONE E INTERFACCIA ---
def formatta_tabella(studenti: list[dict]) -> str:
    """Formatta la lista come stringa a righe indicizzate."""
    if not studenti:
        return "Nessuno studente presente in archivio."
    righe = [f"{'Indice':<8} {'Nome':<25} {'Voto'}", "-" * 40]
    for indice, studente in enumerate(studenti):
        righe.append(f"{indice:<8} {studente['nome']:<25} {studente['voto']:.1f}")
    return "\n".join(righe)


def main() -> None:
    studenti = carica_studenti()
    print(f"Benvenuto. Caricati {len(studenti)} studenti dall'archivio.")

    while True:
        print("\n=== GESTIONALE STUDENTI ===")
        print("1. Visualizza elenco completo")
        print("2. Aggiungi studente")
        print("3. Cerca per nome")
        print("4. Filtra per intervallo voti")
        print("5. Modifica voto studente")
        print("6. Elimina studente")
        print("7. Mostra statistiche")
        print("8. Salva ed Esci")

        scelta = input("\nSeleziona un'operazione (1-8): ").strip()

        if scelta == "1":
            print("\n" + formatta_tabella(studenti))
        elif scelta == "2":
            nome = input("Nome studente: ").strip()
            if not nome:
                print("Errore: il nome non può essere vuoto.")
                continue
            voto_str = input("Voto (0-10): ")
            valido, risultato = valida_voto(voto_str)
            if not valido:
                print(f"Errore: {risultato}")
                continue
            studenti.append({"nome": nome, "voto": float(risultato)})
            print(f"Studente '{nome}' aggiunto con successo.")
        elif scelta == "3":
            termine = input("Inserisci il nome (o parte di esso) da cercare: ")
            print("\n" + formatta_tabella(cerca_per_nome(studenti, termine)))
        elif scelta == "4":
            try:
                min_voto = float(input("Voto minimo: "))
                max_voto = float(input("Voto massimo: "))
                print("\n" + formatta_tabella(filtra_per_voti(studenti, min_voto, max_voto)))
            except ValueError:
                print("Errore: inserisci numeri validi.")
        elif scelta == "5":
            print("\n" + formatta_tabella(studenti))
            try:
                indice = int(input("Inserisci l'indice dello studente da modificare: "))
                if 0 <= indice < len(studenti):
                    voto_str = input(f"Nuovo voto per {studenti[indice]['nome']}: ")
                    valido, risultato = valida_voto(voto_str)
                    if valido:
                        studenti[indice]["voto"] = float(risultato)
                        print("Voto aggiornato con successo.")
                    else:
                        print(f"Errore: {risultato}")
                else:
                    print("Errore: indice fuori range.")
            except ValueError:
                print("Errore: indice non valido.")
        elif scelta == "6":
            print("\n" + formatta_tabella(studenti))
            try:
                indice = int(input("Inserisci l'indice dello studente da eliminare: "))
                if 0 <= indice < len(studenti):
                    rimosso = studenti.pop(indice)
                    print(f"Studente '{rimosso['nome']}' eliminato.")
                else:
                    print("Errore: indice fuori range.")
            except ValueError:
                print("Errore: indice non valido.")
        elif scelta == "7":
            statistiche = calcola_statistiche(studenti)
            print("\n--- STATISTICHE ARCHIVIO ---")
            print(f"Studenti totali: {statistiche['totale']}")
            print(f"Media generale:  {statistiche['media']:.2f}")
            if statistiche["migliore"]:
                print(f"Miglior studente: {statistiche['migliore']['nome']} ({statistiche['migliore']['voto']})")
                print(f"Voto più basso:   {statistiche['peggiore']['nome']} ({statistiche['peggiore']['voto']})")
        elif scelta == "8":
            salva_studenti(studenti)
            print("Dati salvati su 'studenti.json'. Arrivederci!")
            break
        else:
            print("Opzione non valida, riprova.")


if __name__ == "__main__":
    main()
