# Esercizio 02: Scheda Profilo e Accesso Difensivo con .get()

> **Prerequisiti teorici**: Modulo 03 (Cap. 02 - Dizionari e Dati Strutturati)  
> **Obiettivo**: Modellare un'entità del mondo reale tramite dizionario e gestire campi opzionali senza causare `KeyError`.

## Obiettivo
Scrivere due funzioni per creare e leggere una scheda utente:
1. `crea_profilo(nome: str, eta: int, email: str | None = None) -> dict`:
   Costruisce e restituisce un dizionario con chiavi `"nome"` ed `"eta"`. Se `email` non è `None`, aggiunge anche la chiave `"email"`.
2. `estrai_contatto(profilo: dict) -> str`:
   Legge l'indirizzo email associato al profilo usando il metodo `.get()`. Se l'email non è registrata, restituisce la stringa di default: `"Nessuna email registrata"`.

## Istruzioni
- Non accedere mai alla chiave con `profilo["email"]` senza prima verificare la sua esistenza, per evitare crash da `KeyError`.
- Usa la sintassi `profilo.get("email", "Nessuna email registrata")`.

## Esempio di Utilizzo
```python
utente_a = crea_profilo("Mario", 30, "mario@example.com")
utente_b = crea_profilo("Anna", 22)

print(estrai_contatto(utente_a))  # "mario@example.com"
print(estrai_contatto(utente_b))  # "Nessuna email registrata"
```
