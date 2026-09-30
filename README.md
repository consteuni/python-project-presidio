# Template Project for Python

## Esecuzione

Lo script legge il testo dal campo `text` o `content` di un file JSON esterno.

```json
{
  "text": "Mi chiamo Marco Rossi e vivo a Roma."
}
```

Sono supportati anche i JSON di Azure Document Intelligence, dove il testo si trova in `analyzeResult.content`.

Esecuzione:

```bash
uv run python src/presidio-transformers.py percorso/input.json
```

## Devcontainer

Alla creazione del container, `postCreateCommand` esegue `uv python install`
per installare la versione di Python indicata in `.python-version` (3.12),
poi `uv sync --all-groups` e l'installazione di Codex.
Per applicare modifiche alla configurazione, eseguire **Dev Containers: Rebuild Container**.
