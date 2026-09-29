# Template Project for Python

## Esecuzione

Lo script legge il testo dal campo `text` di un file JSON esterno:

```json
{
  "text": "Mi chiamo Marco Rossi e vivo a Roma."
}
```

Esecuzione:

```bash
uv run python src/presidio-transformers.py percorso/input.json
```

## Devcontainer

Alla creazione del container, `postCreateCommand` esegue `uv python install`
per installare la versione di Python indicata in `.python-version` (3.12),
poi `uv sync --all-groups` e l'installazione di Codex.
Per applicare modifiche alla configurazione, eseguire **Dev Containers: Rebuild Container**.
