
from gliner import GLiNER
from presidio_analyzer import EntityRecognizer, RecognizerResult
from presidio_analyzer.nlp_engine import NlpArtifacts


class GLiNERRecognizer(EntityRecognizer):
    """Custom Presidio recognizer using GLiNER for NER."""

    def __init__(
        self,
        supported_entities: list[str] | None = None,
        model_name: str = "urchade/gliner_multi_pii-v1",
        threshold: float = 0.5,
    ) -> None:
        super().__init__(
            supported_entities=supported_entities or ["PERSON", "LOCATION", "ORGANIZATION"],
            name="GLiNERRecognizer",
            supported_language="it",
        )
        self.model_name = model_name
        self.threshold = threshold
        self._model: GLiNER | None = None

    @property
    def model(self) -> GLiNER:
        if self._model is None:
            self._model = GLiNER.from_pretrained(self.model_name)
        return self._model

    def load(self) -> None:
        pass

    def analyze(
        self,
        text: str,
        entities: list[str],
        nlp_artifacts: NlpArtifacts | None = None,
    ) -> list[RecognizerResult]:
        results = []
        predictions = self.model.predict_entities(
            text,
            labels=entities,
            threshold=self.threshold,
        )
        for pred in predictions:
            results.append(
                RecognizerResult(
                    entity_type=pred["label"],
                    start=pred["start"],
                    end=pred["end"],
                    score=pred["score"],
                )
            )
        return results
