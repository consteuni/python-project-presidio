# Project State

Aggiornato: 2026-09-29 · Branch: main · Stato: in corso

## Obiettivo corrente

Sperimentare il riconoscimento e l'anonimizzazione di dati personali con Presidio,
partendo dagli esempi Python presenti, incluso un transformer compatto.

## Stato sintetico

- Stato: in corso.
- Ultima attività completata: aggiunti recognizer regex per identificativi clinici e numeri cartella.
- Prossima attività: verificare end-to-end gli identificativi regex sui referti.

## Architettura rilevante

- `src/presidio-test.py`: esempio in inglese con motore predefinito e riconoscimento di un telefono.
- `src/presidio-transformers.py`: esempio italiano con `it_core_news_sm`, GLiNER, anonimizzazione ed esportazione JSON.
- `src/regex_recognizers.py`: recognizer regex per identificativi clinici strutturati.
- `input/referti/`: referti JSON con campo `content` usati per ricavare i formati reali.
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
- [x] Divisi i testi lunghi in chunk sovrapposti e rimappati gli offset delle entità.
- [x] Aggiunti pattern per tessera sanitaria, identificativo paziente, polizza, protocollo e numero cartella clinica.
- [x] `EPISODE_INFO` supporta numeri cartella da 10 o 12 cifre, incluso il prefisso `01`.
- [x] Analizzati i referti presenti in `input/referti/`.

## Output JSON

- Directory `output/` nella root del progetto, creata automaticamente.
- Campi: `timestamp` (ISO 8601 UTC), `language`, `models`, `original_text`, `analyzer_results`, `anonymized_text`.
- Ogni entità contiene tipo, inizio, fine e punteggio; il JSON include il testo originale.
- Nome con microsecondi; apertura esclusiva per non sovrascrivere file esistenti.
- UTF-8 con accenti leggibili; errori di scrittura propagati al chiamante.

## Prossimi passi

1. Eseguire una verifica end-to-end sui referti e controllare eventuali falsi positivi.

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
- `uv run python src/presidio-transformers.py input/example3.json`: superato senza warning di troncamento GLiNER.
- `uv run ruff check src/regex_recognizers.py src/presidio-transformers.py`: superato.
- `uv run ruff format --check src/regex_recognizers.py src/presidio-transformers.py`: superato.
- Test end-to-end sui referti: non ancora completato.

## Assunzioni da verificare

- [ ] Dipendenze e modello GLiNER necessari disponibili nell'ambiente di esecuzione.
- [x] Inferenza GLiNER e anonimizzazione funzionanti end-to-end.
- [ ] I numeri cartella sono sempre preceduti da `Numero Cartella` o da una variante gestibile.
- [ ] I codici regex non entrano in conflitto con i recognizer generici di Presidio.
- L’esempio GLiNER è in italiano; l’esempio base resta in inglese.
