# Progetto 03: Gestionale Studenti Interattivo con Persistenza JSON

> **Prerequisiti teorici**: Modulo 03 (CRUD su Liste di Record, JSON) e Modulo 05 (Problem Solving)  
> **Obiettivo**: Realizzare un'applicazione software completa a menu con separazione assoluta tra logica pura e I/O di interfaccia.

## I Requisiti del Committente
Creare un'applicazione a console per gestire la segreteria scolastica. I dati devono essere salvati permanentemente nel file `studenti.json`.

## Regole di Architettura Software
- **Nessuna funzione di elaborazione o validazione deve fare `print()`**: devono restituire tuple di stato `(success: bool, messaggio: str, dati)` oppure liste/numeri.
- **Tutte le interazioni con l'utente umano (`input` e `print`) avvengono esclusivamente nel `main()`** o dentro specifiche funzioni di presentazione.

## Menu Principale
```text
=== GESTIONALE STUDENTI ===
1. Aggiungi studente
2. Visualizza elenco completo
3. Cerca per nome (case-insensitive)
4. Filtra per intervallo voti (range min-max)
5. Modifica voto studente
6. Elimina studente
7. Statistiche generali (media, migliore, peggiore)
8. Salva ed Esci
```
