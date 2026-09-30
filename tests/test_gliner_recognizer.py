import re

import pytest
from presidio_analyzer import RecognizerResult

from gliner_recognizer import GLiNERRecognizer
from regex_recognizers import ItalianPhoneRecognizer
from result_resolver import anonymize_results, resolve_results


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


@pytest.mark.parametrize(
    "value",
    ["3331234567", "+39 333 1234567", "02 1234567", "06-12345678"],
)
def test_italian_phone_patterns_match_phone_formats(value: str) -> None:
    recognizer = ItalianPhoneRecognizer()

    assert any(re.fullmatch(pattern.regex, value) for pattern in recognizer.patterns)


@pytest.mark.parametrize("value", ["1234567890", "0123456789", "001234567890"])
def test_italian_phone_patterns_reject_ambiguous_numeric_ids(value: str) -> None:
    recognizer = ItalianPhoneRecognizer()

    assert not any(re.fullmatch(pattern.regex, value) for pattern in recognizer.patterns)


def test_deterministic_identifier_wins_over_overlapping_phone() -> None:
    results = [
        RecognizerResult("PHONE_NUMBER", 6, 12, 0.4),
        RecognizerResult("CLINICAL_IDENTIFIER", 0, 12, 1.0),
    ]

    selected = resolve_results(results)

    assert [(item.entity_type, item.start, item.end) for item in selected] == [
        ("CLINICAL_IDENTIFIER", 0, 12)
    ]


def test_low_score_non_italian_phone_is_filtered() -> None:
    results = [RecognizerResult("PHONE_NUMBER", 0, 8, 0.4)]

    assert resolve_results(results, text="022643.1") == []


def test_low_score_semantic_entities_are_filtered() -> None:
    results = [
        RecognizerResult("PERSON", 0, 5, 0.85),
        RecognizerResult("PERSON", 6, 11, 0.95),
        RecognizerResult("DATE_TIME", 12, 22, 0.5),
    ]

    selected = resolve_results(results)

    assert [(item.entity_type, item.start) for item in selected] == [
        ("PERSON", 6),
        ("DATE_TIME", 12),
    ]


def test_fiscal_code_wins_over_vat_code_on_same_span() -> None:
    results = [
        RecognizerResult("IT_VAT_CODE", 0, 16, 1.0),
        RecognizerResult("IT_FISCAL_CODE", 0, 16, 0.98),
    ]

    selected = resolve_results(results)

    assert [item.entity_type for item in selected] == ["IT_FISCAL_CODE"]


def test_anonymize_results_replaces_from_right_to_left() -> None:
    results = [
        RecognizerResult("PERSON", 0, 5, 1.0),
        RecognizerResult("PHONE_NUMBER", 10, 20, 1.0),
    ]

    assert anonymize_results("Marco abc 3331234567", results) == ("<PERSON> abc <PHONE_NUMBER>")
