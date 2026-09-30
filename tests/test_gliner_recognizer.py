import pytest

from gliner_recognizer import GLiNERRecognizer


def test_threshold_is_applied_per_entity() -> None:
    recognizer = GLiNERRecognizer(
        threshold=0.9,
        thresholds={"PERSON": 0.95},
    )

    assert recognizer._threshold_for("PERSON") == 0.95
    assert recognizer._threshold_for("ADDRESS") == 0.9


@pytest.mark.parametrize(
    ("score", "accepted"),
    [(0.8999, False), (0.9, True), (0.97, True)],
)
def test_entity_threshold(score: float, accepted: bool) -> None:
    recognizer = GLiNERRecognizer(threshold=0.9)

    assert recognizer._accept_prediction({"label": "PERSON", "score": score}) is accepted


def test_invalid_entity_threshold() -> None:
    with pytest.raises(ValueError, match="Soglia non valida"):
        GLiNERRecognizer(thresholds={"PERSON": 1.1})
