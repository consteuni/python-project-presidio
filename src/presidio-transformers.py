"""Esempio Presidio con DistilBERT NER per testi in inglese."""

from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import TransformersNlpEngine
from presidio_anonymizer import AnonymizerEngine


def main() -> None:
    text = "My name is Don and my phone number is 212-555-5555"

    # spaCy gestisce token e lemmi; DistilBERT riconosce le entità.
    # I modelli vengono scaricati al primo utilizzo, se non già presenti.
    model_config = [
        {
            "lang_code": "en",
            "model_name": {
                "spacy": "en_core_web_sm",
                "transformers": "dslim/distilbert-NER",
            },
        }
    ]
    nlp_engine = TransformersNlpEngine(models=model_config)
    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["en"])

    # Presidio combina il modello NER con gli altri riconoscitori (es. telefoni).
    results = analyzer.analyze(text=text, language="en")
    anonymized = AnonymizerEngine().anonymize(text=text, analyzer_results=results)

    print(f"Testo originale: {text}")
    print(f"Entità rilevate: {results}")
    print(f"Testo anonimizzato: {anonymized.text}")


if __name__ == "__main__":
    main()
