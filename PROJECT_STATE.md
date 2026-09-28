# Project State

Ultimo aggiornamento: 2026-09-28
Branch: main
Checkpoint: esportazione JSON con timestamp

## Obiettivo corrente

Sperimentare il riconoscimento e l'anonimizzazione di dati personali con Presidio,
partendo dagli esempi Python presenti, incluso un transformer compatto.

## Stato sintetico

- Stato: in corso, progetto appena avviato.
- Ultima attività completata: aggiunto il salvataggio JSON dei risultati con timestamp UTC.
- Prossima attività: verificare dipendenze e avvio dell'esempio DistilBERT.
- Blocco principale: nessuno accertato; ambiente e inferenza da verificare.
- L'assenza iniziale di questo documento era normale: non esiste uno stato precedente da recuperare.

## Architettura rilevante

- `src/presidio-test.py`: esempio in inglese con motore predefinito e riconoscimento di un telefono.
- `src/presidio-transformers.py`: esempio italiano con `it_core_news_sm`, `osiria/distilbert-italian-cased-ner`, anonimizzazione ed esportazione JSON.
- `pyproject.toml`: Python 3.12, dipendenze Presidio con extra Transformers, pytest e Ruff.
- `uv.lock`: lockfile presente; sincronizzazione dell'ambiente da verificare.

## Attività completate

- [x] Verificata la presenza dei due esempi e delle dipendenze dichiarate.
- [x] Inizializzata la memoria operativa del nuovo progetto.

- [x] Configurato uv in modalità copia e validata la sintassi TOML.

- [x] Aggiunto salvataggio in `output/presidio-transformers_<timestamp-UTC>.json`.

## Output JSON

- Directory `output/` nella root del progetto, creata automaticamente.
- Campi: `timestamp` (ISO 8601 UTC), `language`, `models`, `original_text`, `analyzer_results`, `anonymized_text`.
- Ogni entità contiene tipo, inizio, fine e punteggio; il JSON include il testo originale.
- Nome con microsecondi; apertura esclusiva per non sovrascrivere file esistenti.
- UTF-8 con accenti leggibili; errori di scrittura propagati al chiamante.

## Prossimi passi

1. Verificare l'ambiente uv e avviare `uv run python src/presidio-transformers.py`; registrare l'esito e correggere eventuali problemi di avvio.
2. Verificare rilevamento e anonimizzazione sul testo dimostrativo, eseguendo i controlli pertinenti alle eventuali modifiche.
3. Documentare nel README i comandi di installazione e avvio verificati.

## Comandi utili

```bash
uv sync
uv run python src/presidio-transformers.py
uv run ruff check src/presidio-transformers.py
uv run ruff format --check src/presidio-transformers.py
```

## Verifiche eseguite

- `.venv/bin/ruff check src/presidio-transformers.py`: superato.
- `.venv/bin/ruff format --check src/presidio-transformers.py`: superato.
- Compilazione con `compile`: superata.
- Smoke test del salvataggio in directory temporanea con motori simulati e import NLP esclusi: superati JSON, Unicode, timestamp UTC, lista entità vuota e file distinti.
- `git diff --check -- src/presidio-transformers.py PROJECT_STATE.md`: superato; diff revisionato.

- Parsing di `pyproject.toml` con `tomllib` e verifica di `tool.uv.link-mode`: superati.
- `git diff --check -- pyproject.toml PROJECT_STATE.md`: superato.

- Lettura delle istruzioni, del README, degli esempi e di `pyproject.toml`: completata.
- Stato Git iniziale e finale: controllato, modifiche preesistenti preservate.
- Diff di questo checkpoint: revisionato, nessun secret introdotto.
- Controllo whitespace del documento con `git diff --no-index --check`: superato.

## Verifiche non eseguite

- `uv run python src/presidio-transformers.py`: inferenza reale non eseguita in questo checkpoint; verifica del salvataggio separata dai modelli.
- Installazione dei pacchetti non rieseguita: la modalità copia sarà usata nelle prossime installazioni.

## Assunzioni da verificare

- [ ] Dipendenze e modelli necessari disponibili nell'ambiente di esecuzione.
- [ ] Inferenza e anonimizzazione funzionanti end-to-end.
- L’esempio Transformers attuale è in italiano; l’esempio base resta in inglese.
