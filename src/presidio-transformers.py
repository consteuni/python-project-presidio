import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine
from presidio_anonymizer import AnonymizerEngine

from gliner_recognizer import GLiNERRecognizer
from regex_recognizers import ClinicalIdentifierRecognizer, EpisodeInfoRecognizer


def load_text(input_path: Path) -> str:
    try:
        with input_path.open(encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise ValueError(f"File JSON non trovato: {input_path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON non valido in {input_path}: {error.msg}") from error

    text = None
    if isinstance(data, dict):
        text = data.get("text")
        if text is None:
            text = data.get("content")
        if text is None and isinstance(data.get("analyzeResult"), dict):
            text = data["analyzeResult"].get("content")
    if not isinstance(text, str):
        raise ValueError(
            "Il JSON deve contenere il campo stringa 'text' o 'content' "
            "(anche in 'analyzeResult')"
        )
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Analizza e anonimizza il testo di un file JSON.")
    parser.add_argument(
        "input_json",
        type=Path,
        help="File JSON contenente 'text' o 'content' come stringa",
    )
    args = parser.parse_args()
    try:
        text = load_text(args.input_json)
    except ValueError as error:
        parser.error(str(error))

    models = [
        {
            "lang_code": "it",
            "model_name": "it_core_news_sm",
        }
    ]

    nlp_engine = SpacyNlpEngine(models=models)
    analyzer = AnalyzerEngine(
        nlp_engine=nlp_engine,
        supported_languages=["it"],
    )
    analyzer.registry.add_recognizer(ClinicalIdentifierRecognizer())
    analyzer.registry.add_recognizer(EpisodeInfoRecognizer())
    analyzer.registry.add_recognizer(
        GLiNERRecognizer(
            threshold=0.9,
            thresholds={
                "PERSON": 0.9,
                "LOCATION": 0.9,
                "ORGANIZATION": 0.9,
                "ADDRESS": 0.9,
                "PROFESSION": 0.9,
            },
        )
    )

    results = analyzer.analyze(text=text, language="it")
    anonymized = AnonymizerEngine().anonymize(
        text=text,
        analyzer_results=results,
    )

    timestamp = datetime.now(UTC)
    output = {
        "timestamp": timestamp.isoformat(),
        "language": "it",
        "models": {
            "nlp": models,
            "gliner": "urchade/gliner_multi_pii-v1",
        },
        "original_text": text,
        "analyzer_results": [
            {
                "entity_type": result.entity_type,
                "start": int(result.start),
                "end": int(result.end),
                "score": float(result.score),
            }
            for result in results
        ],
        "anonymized_text": anonymized.text,
    }
    output_dir = Path(__file__).resolve().parent.parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"presidio-transformers_{timestamp:%Y%m%dT%H%M%S_%fZ}.json"
    with output_path.open("x", encoding="utf-8") as file:
        json.dump(output, file, ensure_ascii=False, indent=2, allow_nan=False)
        file.write("\n")

    print(f"Testo originale: {text}")
    print(f"Entità rilevate: {results}")
    print(f"Testo anonimizzato: {anonymized.text}")
    print(f"Output JSON salvato in: {output_path}")


if __name__ == "__main__":
    main()
