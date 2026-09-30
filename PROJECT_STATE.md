# Project State

Aggiornato: 2026-09-30 · Branch: main · Stato: in corso

## Obiettivo corrente

Sperimentare il riconoscimento e l'anonimizzazione di dati personali con Presidio,
partendo dagli esempi Python presenti, incluso un transformer compatto.

## Stato sintetico

- Stato: in corso.
- Ultima attività completata: testati tutti i 13 referti disponibili dopo il filtro semantico.
- Prossima attività: filtrare i `PHONE_NUMBER` a score 0.4 non conformi al formato telefonico italiano.

## Architettura rilevante

- `src/presidio-test.py`: esempio in inglese con motore predefinito e riconoscimento di un telefono.
- `src/presidio-transformers.py`: esempio italiano con `it_core_news_sm`, GLiNER, anonimizzazione ed esportazione JSON.
- `src/regex_recognizers.py`: recognizer regex per identificativi clinici strutturati e telefoni italiani.
- `src/result_resolver.py`: priorità, deduplicazione e sostituzione non sovrapposta degli span.
- `tests/test_gliner_recognizer.py`: test delle soglie e del filtraggio delle predizioni GLiNER.
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
- [x] Supportata la lettura dei campi `text`, `content` e `analyzeResult.content`.
- [x] Valutato `output/presidio-transformers_20260929T152812_055943Z.json`.
- [x] Verificata l'anonimizzazione del nome paziente, contatti, indirizzi, date e numeri cartella.
- [x] Impostata soglia GLiNER predefinita a `0.9` con override per entità.
- [x] Mantenuti attivi i recognizer standard e regex di Presidio.
- [x] Aggiunti test unitari per soglie valide, invalide e predizioni filtrate.
- [x] Aggiunto `ItalianPhoneRecognizer` per cellulari e fissi italiani.
- [x] Validata l’inferenza su `input/example.json`: 18 entità, testo anonimizzato e JSON generato.
- [x] Verificato il riconoscimento del cellulare italiano con score 0.99.
- [x] Aggiunta risoluzione degli span con priorità agli identificativi deterministici.
- [x] Validati i referti `1.json` e `2.json` con 0 sovrapposizioni e 0 telefoni a score basso.
- [x] Confrontati output prima/dopo: referto 1 da 51 a 42 entità, referto 2 da 39 a 30, mantenendo i codici fiscali.
- [x] Valutata la qualità semantica: molti `PERSON`, `LOCATION` e `ORGANIZATION` a score 0.85 sono falsi positivi su intestazioni, HTML e termini clinici.
- [x] Filtrati gli score semantici sotto 0.9: referto 1 da 42 a 17 entità, referto 2 da 30 a 12, mantenendo i nominativi ad alta confidenza.
- [x] Suite completa passata: 16 test.
- [x] Validato `input/example.json`: 13 entità, 2 telefoni, codice fiscale e identificativi clinici preservati.
- [x] Testati 13 referti: 13/13 senza sovrapposizioni e span non validi; rilevati 8 telefoni a score 0.4, tutti codici o sequenze non conformi al formato italiano.

## Output JSON

- Directory `output/` nella root del progetto, creata automaticamente.
- Campi: `timestamp` (ISO 8601 UTC), `language`, `models`, `original_text`, `analyzer_results`, `anonymized_text`.
- Ogni entità contiene tipo, inizio, fine e punteggio; il JSON include il testo originale.
- Nome con microsecondi; apertura esclusiva per non sovrascrivere file esistenti.
- UTF-8 con accenti leggibili; errori di scrittura propagati al chiamante.

## Prossimi passi

1. Filtrare i `PHONE_NUMBER` a score 0.4 non conformi al formato italiano.
2. Aggiungere fixture strutturali per i referti testati.
3. Ripetere il test end-to-end e verificare la copertura dei telefoni reali.

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
- `uv run ruff check src/gliner_recognizer.py src/presidio-transformers.py tests/test_gliner_recognizer.py`: superato dopo correzione della nuova riga lunga.
- `python -m py_compile src/gliner_recognizer.py src/presidio-transformers.py tests/test_gliner_recognizer.py`: superato.
- `uv run ruff format --check src/regex_recognizers.py src/presidio-transformers.py`: superato.
- `python -m py_compile src/presidio-transformers.py`: superato.
- `git diff --check`: superato.
- Test su `output/presidio-transformers_20260929T152812_055943Z.json`: copertura dei dati diretti buona, falsi positivi numerosi.
- `uv run pytest tests/test_gliner_recognizer.py`: superato, 12 test.
- `uv run python src/presidio-transformers.py input/example.json`: superato; output `presidio-transformers_20260930T091847_258889Z.json` generato.
- `uv run python src/presidio-transformers.py input/referti_test/HSR.DNSAN035_6_Dimissione_1/1.json`: superato; 42 entità applicate, 2 telefoni, 1 episodio, 0 sovrapposizioni.
- `uv run python src/presidio-transformers.py input/referti_test/HSR.DNSAN035_6_Dimissione_1/2.json`: superato; 30 entità applicate, 3 telefoni, 1 episodio, 0 sovrapposizioni.
- Output finali: `presidio-transformers_20260930T095005_185962Z.json` e `presidio-transformers_20260930T095031_363012Z.json`.
- Output filtrati: `presidio-transformers_20260930T100512_717958Z.json` e `presidio-transformers_20260930T100543_524094Z.json`.
- Output regressione: `presidio-transformers_20260930T111532_393385Z.json`.

## Assunzioni da verificare

- [x] Dipendenze e modello GLiNER necessari disponibili nell'ambiente di esecuzione.
- [x] Inferenza GLiNER e anonimizzazione funzionanti end-to-end.
- [ ] I numeri cartella sono sempre preceduti da `Numero Cartella` o da una variante gestibile.
- [x] I codici regex non entrano in conflitto con i recognizer generici di Presidio.

## Problemi noti

- GLiNER con soglia attuale produce falsi positivi su parole comuni, intestazioni e nomi di esami (`Paziente`, `Esame`, `S-SODIO`, ecc.).
- Il resolver elimina i `PHONE_NUMBER` a basso score quando sovrapposti a identificativi deterministici.
- GLiNER produce ancora falsi positivi residui su entità semantiche cliniche; da valutare caso per caso.
- In alcuni casi GLiNER classifica frasi cliniche come `CLINICAL_IDENTIFIER`; l'output resta semanticamente degradato anche quando i dati personali sono coperti.

### Nota per i test successivi

La valutazione del referto `output/presidio-transformers_20260929T152812_055943Z.json` è la baseline di riferimento: la copertura dei dati personali e di `EPISODE_INFO` è buona, ma i falsi positivi GLiNER sono numerosi e riducono la qualità clinica dell'output. Questi risultati servono per confrontare ogni modifica a soglia, filtraggio o recognizer.

## Decisioni

- `EPISODE_INFO` riconosce solo numeri associati alla dicitura `Numero Cartella`, con lunghezza 10 o 12 cifre, per evitare catture generiche.
- GLiNER usa soglia `0.9` per default; le soglie per entità possono sovrascriverla e il filtraggio avviene solo nel recognizer GLiNER.
