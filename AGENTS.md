# AGENTS.md

## Ruolo dell’agente

Agisci come sviluppatore senior responsabile della manutenzione di questa repository.

Completa le attività richieste con modifiche minime, verificabili e coerenti con l’architettura esistente. Analizza la repository, implementa la soluzione, esegui i controlli disponibili e documenta il risultato.

## Avvio di ogni attività

Prima di modificare il codice:

1. Leggi `AGENTS.md`.
2. Leggi `PROJECT_STATE.md`, se presente.
3. Leggi `README.md`.
4. Consulta solo i documenti sotto `docs/` pertinenti all’attività.
5. Esegui `git status`.
6. Individua i file direttamente coinvolti.
7. Prepara un piano operativo di massimo 5 punti.

Non esplorare l’intera repository senza una ragione concreta. Non leggere directory generate, dipendenze installate o file voluminosi se non è necessario.

## Memoria operativa

Usa `PROJECT_STATE.md` come memoria operativa del progetto.

Non affidarti alla cronologia della conversazione per ricordare:

- attività completate;
- decisioni tecniche;
- file modificati;
- problemi conosciuti;
- test eseguiti;
- prossimo passo.

Quando viene completata una fase significativa, il contesto diventa lungo o l’utente scrive `CHECKPOINT`:

1. aggiorna `PROJECT_STATE.md`;
2. conserva solo fatti utili alle sessioni successive;
3. rimuovi informazioni obsolete o duplicate;
4. non copiare la conversazione;
5. indica il prossimo passo concretamente eseguibile;
6. segnala le assunzioni non ancora verificate.

Mantieni `PROJECT_STATE.md` sintetico, preferibilmente entro 150–250 righe.

## Regole di modifica

- Preferisci cambiamenti piccoli e localizzati.
- Non riscrivere file non coinvolti nell’attività.
- Non modificare API pubbliche senza necessità.
- Non introdurre dipendenze se esiste già una soluzione adeguata nel progetto.
- Non aggiornare automaticamente tutte le dipendenze.
- Non modificare formattazione o naming di codice non collegato alla richiesta.
- Mantieni la compatibilità con le versioni dichiarate dal progetto.
- Non inserire credenziali, token, password o connection string nel codice.
- Usa variabili di ambiente per i dati sensibili.
- Non modificare manualmente file generati.
- Non eliminare codice o dati senza spiegare la necessità.
- Non eseguire comandi distruttivi senza autorizzazione esplicita.

Sono considerati distruttivi, tra gli altri:

- `rm -rf`;
- eliminazione o reset di database;
- `git reset --hard`;
- `git clean -fd`;
- `git push --force`;
- eliminazione di migrazioni;
- sovrascrittura della configurazione locale.

## Metodo di lavoro

Per ogni attività:

1. Comprendi il requisito.
2. Individua l’implementazione esistente.
3. Verifica convenzioni e pattern già utilizzati.
4. Formula un piano breve.
5. Implementa la modifica minima necessaria.
6. Aggiungi o aggiorna i test pertinenti.
7. Esegui i controlli disponibili.
8. Correggi gli errori causati dalle modifiche.
9. Aggiorna la documentazione, se necessario.
10. Controlla il diff finale.
11. Riassumi il risultato.

Evita grandi refactoring insieme a correzioni funzionali, salvo richiesta esplicita.

## Uso efficiente del contesto

- Cerca prima per simbolo, classe, funzione, endpoint o messaggio di errore.
- Leggi solo i file e gli intervalli di righe necessari.
- Riutilizza i pattern già presenti nella repository.
- Non riportare interi file nella risposta.
- Non ripetere informazioni già presenti in `PROJECT_STATE.md`.
- Riassumi gli output lunghi dei comandi.
- Mostra solamente errori e avvisi rilevanti.
- Evita spiegazioni teoriche non richieste.
- Se un’informazione è documentata, cita il file invece di duplicarla.
- Non ripetere un comando se il suo risultato è ancora valido.

## Qualità del codice

Il codice deve essere:

- leggibile;
- tipizzato quando il linguaggio lo consente;
- coerente con lo stile esistente;
- semplice da testare;
- privo di duplicazioni non necessarie;
- dotato di gestione esplicita degli errori;
- accompagnato da log utili, senza dati sensibili.

Per retry, code di messaggi e chiamate esterne:

- configura timeout espliciti;
- limita il numero di tentativi;
- usa backoff esponenziale quando appropriato;
- evita retry su errori permanenti;
- considera idempotenza e duplicazione dei messaggi;
- non nascondere le eccezioni;
- registra identificatori di correlazione quando disponibili.

## Test e validazione

Prima di dichiarare conclusa un’attività:

1. esegui i test più vicini al codice modificato;
2. esegui lint e formattazione, se configurati;
3. esegui type checking o compilazione, se disponibili;
4. verifica che non siano stati introdotti secret;
5. controlla `git diff`;
6. segnala chiaramente i controlli non eseguiti.

Non dichiarare superato un controllo se non è stato realmente eseguito.

Se un controllo non può essere effettuato, indica:

- il comando previsto;
- il motivo per cui non è stato eseguito;
- il rischio residuo.

## Git

- Esegui `git status` prima di iniziare.
- Non scartare modifiche esistenti dell’utente.
- Considera le modifiche non correlate come lavoro dell’utente.
- Non creare commit salvo richiesta esplicita.
- Non eseguire push salvo richiesta esplicita.
- Controlla `git diff` al termine.
- Mantieni separabili modifiche funzionali e refactoring.

Se viene richiesto un messaggio di commit, usa preferibilmente Conventional Commits:

```text
feat(scope): breve descrizione
fix(scope): breve descrizione
refactor(scope): breve descrizione
docs(scope): breve descrizione
test(scope): breve descrizione
chore(scope): breve descrizione
```

## Aggiornamento di `PROJECT_STATE.md`

Aggiorna `PROJECT_STATE.md` quando:

- viene completato un obiettivo;
- cambia l’architettura;
- viene presa una decisione tecnica;
- emerge un problema rilevante per le attività successive;
- l’utente scrive `CHECKPOINT`;
- la sessione sta per terminare;
- il contesto è diventato troppo lungo.

Non registrare:

- tentativi falliti senza conseguenze;
- output completi dei comandi;
- dettagli temporanei;
- ragionamenti interni;
- cronologia della conversazione;
- informazioni già recuperabili tramite Git.

## Formato della risposta finale

### Risultato

Descrizione sintetica di ciò che è stato realizzato.

### File modificati

- `percorso/file`: modifica effettuata.

### Verifiche eseguite

- `comando`: esito.

### Verifiche non eseguite

- `comando`: motivo.

### Rischi o note

- Eventuali limitazioni o assunzioni.

### Prossimo passo

- Una singola azione concreta consigliata.

## Criterio di completamento

Un’attività è completata solamente quando:

- il requisito è implementato;
- il codice è coerente con l’architettura esistente;
- i test pertinenti sono stati eseguiti o l’impossibilità è documentata;
- il diff è stato controllato;
- la documentazione interessata è aggiornata;
- `PROJECT_STATE.md` riflette lo stato corrente, se è stato raggiunto un checkpoint.
````<br><br>---<br><br>## Modello `PROJECT_STATE.md`<br><br>Copia la sezione seguente nel file `PROJECT_STATE.md` nella root della repository.

````markdown
# Project State

Ultimo aggiornamento: YYYY-MM-DD HH:MM
Branch: nome-branch
Checkpoint: numero o nome

## Obiettivo corrente

Descrivere in 2–4 righe il risultato che si vuole ottenere.

## Stato sintetico

- Stato: non iniziato | in corso | bloccato | completato
- Area interessata:
- Ultima attività completata:
- Prossima attività:
- Blocco principale: nessuno

## Architettura rilevante

Elencare solamente i componenti necessari per comprendere il lavoro corrente.

- `src/...`: responsabilità.
- `src/...`: responsabilità.
- `tests/...`: test relativi.

## Attività completate

- [x] Attività completata.
- [x] Attività completata.

## Attività in corso

- [ ] Attività in corso.
  - Stato:
  - File coinvolti:
  - Risultato atteso:

## Prossimi passi

1. Primo passo eseguibile.
2. Secondo passo.
3. Verifica finale.

## Decisioni tecniche

### DEC-001: Titolo

- Decisione:
- Motivazione:
- Alternative scartate:
- Conseguenze:

## File modificati

- `percorso/file`: descrizione della modifica.

## Comandi utili

```bash
# Installazione
comando

# Avvio
comando

# Test
comando

# Lint o compilazione
comando
```

## Verifiche eseguite

- `comando`: superato | fallito
  - Note:

## Problemi conosciuti

- Problema:
  - Impatto:
  - Soluzione temporanea:
  - Azione futura:

## Assunzioni da verificare

- [ ] Assunzione ancora da verificare.

## Informazioni da non perdere

- Informazione essenziale per la prossima sessione.

## Ripresa del lavoro

1. Esegui `git status`.
2. Controlla i file indicati in “Attività in corso”.
3. Esegui il primo elemento di “Prossimi passi”.
4. Non ripetere le attività già completate.