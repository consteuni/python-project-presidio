# Project State

Ultimo aggiornamento: 2026-09-29
Branch: main
Checkpoint: installazione esplicita Python nel devcontainer

## Obiettivo corrente

Sperimentare il riconoscimento e l'anonimizzazione di dati personali con Presidio,
partendo dagli esempi Python presenti, incluso un transformer compatto.

## Stato sintetico

- Stato: completato.
- Ultima attività completata: reso il testo di input configurabile tramite file JSON esterno.
- Prossima attività: nessuna; input JSON e flusso end-to-end sono stati verificati.
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
- [x] Corretto `model_name` da dizionario a stringa per la compatibilità con Presidio.
- [x] Aggiunta lettura del campo `text` da JSON tramite argomento da riga di comando.
- [x] Esteso GLiNER con le entità semantiche `ADDRESS` e `PROFESSION`.

## Output JSON

- Directory `output/` nella root del progetto, creata automaticamente.
- Campi: `timestamp` (ISO 8601 UTC), `language`, `models`, `original_text`, `analyzer_results`, `anonymized_text`.
- Ogni entità contiene tipo, inizio, fine e punteggio; il JSON include il testo originale.
- Nome con microsecondi; apertura esclusiva per non sovrascrivere file esistenti.
- UTF-8 con accenti leggibili; errori di scrittura propagati al chiamante.

## Prossimi passi

1. Fornire un file JSON con campo `text` per eseguire una nuova analisi.

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
- `uv run ruff format --check src/presidio-transformers.py`: superato.
- `uv run pytest`: nessun test raccolto (exit 5).
- `uv run python src/presidio-transformers.py`: superato; rilevate entità, testo anonimizzato e JSON generato.
- `python -m json.tool output/presidio-transformers_20260929T125543_845857Z.json`: superato.
- `uv run python src/presidio-transformers.py input/example.json`: superato.

## Assunzioni da verificare

- [ ] Dipendenze e modello GLiNER necessari disponibili nell'ambiente di esecuzione.
- [x] Inferenza GLiNER e anonimizzazione funzionanti end-to-end.
- L’esempio GLiNER è in italiano; l’esempio base resta in inglese.

## Devcontainer: installazione Codex

- Aggiunto l'installer Codex a `postCreateCommand`, dopo `uv sync --all-groups`.
- Bash con `pipefail` propaga anche gli errori del download.
- Parsing JSON verificato; installazione e rebuild non eseguiti, da verificare nel prossimo container ricreato.

## Devcontainer: installazione Python

- `postCreateCommand` esegue `uv python install` prima di `uv sync --all-groups`.
- La versione resta definita da `.python-version` (3.12), senza fissare la patch.
- README aggiornato con il comportamento di inizializzazione.
- Parsing JSON, ordine dei comandi e sintassi Bash verificati; diff controllato senza nuovi secret.
- Rebuild del container non eseguito dalla sessione: resta da verificare l’installazione nel container ricreato.
