# Project State

Ultimo aggiornamento: 2026-09-28
Branch: main
Checkpoint: stato iniziale del progetto

## Obiettivo corrente

Sperimentare il riconoscimento e l'anonimizzazione di dati personali con Presidio,
partendo dagli esempi Python presenti, incluso un transformer compatto.

## Stato sintetico

- Stato: in corso, progetto appena avviato.
- Ultima attività completata: documentazione dello stato iniziale verificato nei file.
- Prossima attività: verificare dipendenze e avvio dell'esempio DistilBERT.
- Blocco principale: nessuno accertato; ambiente e inferenza da verificare.
- L'assenza iniziale di questo documento era normale: non esiste uno stato precedente da recuperare.

## Architettura rilevante

- `src/presidio-test.py`: esempio in inglese con motore predefinito e riconoscimento di un telefono.
- `src/presidio-transformers.py`: esempio in inglese con `en_core_web_sm`, `dslim/distilbert-NER` e anonimizzazione.
- `pyproject.toml`: Python 3.12, dipendenze Presidio con extra Transformers, pytest e Ruff.
- `uv.lock`: lockfile presente; sincronizzazione dell'ambiente da verificare.

## Attività completate

- [x] Verificata la presenza dei due esempi e delle dipendenze dichiarate.
- [x] Inizializzata la memoria operativa del nuovo progetto.

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

- Lettura delle istruzioni, del README, degli esempi e di `pyproject.toml`: completata.
- Stato Git iniziale e finale: controllato, modifiche preesistenti preservate.
- Diff di questo checkpoint: revisionato, nessun secret introdotto.
- Controllo whitespace del documento con `git diff --no-index --check`: superato.

## Verifiche non eseguite

- `uv run python src/presidio-transformers.py`: rinviato al primo passo operativo; questo checkpoint aggiorna solo la documentazione.
- Test e Ruff: non pertinenti alla sola modifica Markdown.

## Assunzioni da verificare

- [ ] Dipendenze e modelli necessari disponibili nell'ambiente di esecuzione.
- [ ] Inferenza e anonimizzazione funzionanti end-to-end.
- [ ] Lingua dei futuri dati di test: gli esempi attuali sono in inglese.
