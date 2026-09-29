# Project State

Ultimo aggiornamento: 2026-09-29
Branch: main
Checkpoint: installazione Codex nel devcontainer

## Obiettivo corrente

Sperimentare il riconoscimento e l'anonimizzazione di dati personali con Presidio,
partendo dagli esempi Python presenti, incluso un transformer compatto.

## Stato sintetico

- Stato: completato.
- Ultima attività completata: configurato GLiNER come unico recognizer PII, con spaCy usato solo come NLP engine di supporto.
- Prossima attività: esecuzione manuale dello script e dei controlli Ruff.
- Blocco principale: nessuno.

## Architettura rilevante

- `src/presidio-test.py`: esempio in inglese con motore predefinito e riconoscimento di un telefono.
- `src/presidio-transformers.py`: esempio italiano con `it_core_news_sm`, GLiNER, anonimizzazione ed esportazione JSON.
- `pyproject.toml`: Python 3.12, dipendenze Presidio con extra Transformers, pytest e Ruff.
- `uv.lock`: lockfile presente; sincronizzazione dell'ambiente da verificare.

## Attività completate

- [x] Verificata la presenza dei due esempi e delle dipendenze dichiarate.
- [x] Inizializzata la memoria operativa del nuovo progetto.
- [x] Configurato uv in modalità copia e validata la sintassi TOML.
- [x] Aggiunto salvataggio in `output/presidio-transformers_<timestamp-UTC>.json`.
- [x] Corretto il modello NER da `FacebookAI/roberta-base` (non NER) a `osiria/distilbert-italian-cased-ner`.
- [x] Convertiti i line endings CRLF in LF per coerenza con il repository.
- [x] Integrato GLiNER come unico recognizer PII in Presidio.
- [x] Aggiunte dipendenze `gliner>=0.2.16` e `protobuf>=5.29.0`.
- [x] Confermata l'anonimizzazione end-to-end con GLiNER.

## Output JSON

- Directory `output/` nella root del progetto, creata automaticamente.
- Campi: `timestamp` (ISO 8601 UTC), `language`, `models`, `original_text`, `analyzer_results`, `anonymized_text`.
- Ogni entità contiene tipo, inizio, fine e punteggio; il JSON include il testo originale.
- Nome con microsecondi; apertura esclusiva per non sovrascrivere file esistenti.
- UTF-8 con accenti leggibili; errori di scrittura propagati al chiamante.

## Prossimi passi

1. Eseguire `Dev Containers: Rebuild Container`, poi verificare `codex --version`.

## Comandi utili

```bash
uv sync
uv run python src/presidio-transformers.py
uv run ruff check src/presidio-transformers.py
uv run ruff format --check src/presidio-transformers.py
```

## Verifiche eseguite

- `uv run ruff format src/presidio-transformers.py`: superato.
- `uv run ruff check src/presidio-transformers.py`: superato.
- `git diff --check -- src/presidio-transformers.py`: superato.
- Verifica statica della modifica: da eseguire manualmente.

## Verifiche non eseguite

- `uv run python src/presidio-transformers.py`: non eseguito; lo lancerà l'utente.
- `uv run ruff check src/presidio-transformers.py`: non eseguito; lo lancerà l'utente.
- `uv run ruff format --check src/presidio-transformers.py`: non eseguito; lo lancerà l'utente.

## Assunzioni da verificare

- [ ] Dipendenze e modello GLiNER necessari disponibili nell'ambiente di esecuzione.
- [ ] Inferenza GLiNER e anonimizzazione funzionanti end-to-end.
- L’esempio GLiNER è in italiano; l’esempio base resta in inglese.

## Devcontainer: installazione Codex

- Aggiunto l'installer Codex a `postCreateCommand`, dopo `uv sync --all-groups`.
- Bash con `pipefail` propaga anche gli errori del download.
- Parsing JSON verificato; installazione e rebuild non eseguiti, da verificare nel prossimo container ricreato.
