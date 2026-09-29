import json
from datetime import UTC, datetime
from pathlib import Path

from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine
from presidio_anonymizer import AnonymizerEngine

from gliner_recognizer import GLiNERRecognizer


def main() -> None:
    text = "Mi chiamo Marco Rossi e vivo a Roma."

    models = [
        {
            "lang_code": "it",
            "model_name": {
                "spacy": "it_core_news_sm",
            },
        }
    ]

    nlp_engine = SpacyNlpEngine(models=models)
    analyzer = AnalyzerEngine(
        nlp_engine=nlp_engine,
        supported_languages=["it"],
    )
    analyzer.registry.add_recognizer(GLiNERRecognizer())

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
