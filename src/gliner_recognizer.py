from gliner import GLiNER
from presidio_analyzer import EntityRecognizer, RecognizerResult
from presidio_analyzer.nlp_engine import NlpArtifacts


class GLiNERRecognizer(EntityRecognizer):
    """Custom Presidio recognizer using GLiNER for chunked NER."""

    def __init__(
        self,
        supported_entities: list[str] | None = None,
        model_name: str = "urchade/gliner_multi_pii-v1",
        threshold: float = 0.9,
        thresholds: dict[str, float] | None = None,
        max_chunk_chars: int = 1600,
        overlap_chars: int = 150,
    ) -> None:
        super().__init__(
            supported_entities=supported_entities
            or ["PERSON", "LOCATION", "ORGANIZATION", "ADDRESS", "PROFESSION"],
            name="GLiNERRecognizer",
            supported_language="it",
        )
        self.model_name = model_name
        self.threshold = threshold
        self.thresholds = thresholds or {}
        for entity, entity_threshold in self.thresholds.items():
            if not 0 <= entity_threshold <= 1:
                raise ValueError(f"Soglia non valida per {entity}: {entity_threshold}")
        if max_chunk_chars <= overlap_chars:
            raise ValueError("max_chunk_chars deve essere maggiore di overlap_chars")
        self.max_chunk_chars = max_chunk_chars
        self.overlap_chars = overlap_chars
        self._model: GLiNER | None = None

    @property
    def model(self) -> GLiNER:
        if self._model is None:
            self._model = GLiNER.from_pretrained(self.model_name)
        return self._model

    def load(self) -> None:
        pass

    def _threshold_for(self, entity: str) -> float:
        return self.thresholds.get(entity, self.threshold)

    def _accept_prediction(self, prediction: dict[str, object]) -> bool:
        label = prediction["label"]
        score = prediction["score"]
        return (
            isinstance(label, str)
            and isinstance(score, (int, float))
            and score >= self._threshold_for(label)
        )

    def _chunks(self, text: str) -> list[tuple[str, int]]:
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.max_chunk_chars, len(text))
            if end < len(text):
                boundary = text.rfind(" ", start, end)
                if boundary > start:
                    end = boundary
            chunks.append((text[start:end], start))
            if end == len(text):
                break
            start = end - self.overlap_chars
            while start < len(text) and text[start].isspace():
                start += 1
        return chunks

    def analyze(
        self,
        text: str,
        entities: list[str],
        nlp_artifacts: NlpArtifacts | None = None,
    ) -> list[RecognizerResult]:
        results_by_span = {}
        for chunk, offset in self._chunks(text):
            predictions = self.model.predict_entities(
                chunk,
                labels=entities,
                threshold=min(self._threshold_for(entity) for entity in entities),
            )
            for pred in predictions:
                if not self._accept_prediction(pred):
                    continue
                start = offset + pred["start"]
                end = offset + pred["end"]
                key = (pred["label"], start, end)
                result = RecognizerResult(
                    entity_type=pred["label"],
                    start=start,
                    end=end,
                    score=pred["score"],
                )
                previous = results_by_span.get(key)
                if previous is None or result.score > previous.score:
                    results_by_span[key] = result
        return list(results_by_span.values())
