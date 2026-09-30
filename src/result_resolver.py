import re

from presidio_analyzer import RecognizerResult

from regex_recognizers import ItalianPhoneRecognizer

SEMANTIC_ENTITY_TYPES = {"PERSON", "LOCATION", "ORGANIZATION"}
MIN_SEMANTIC_SCORE = 0.9
MIN_PHONE_SCORE = 0.9
ITALIAN_PHONE_PATTERNS = tuple(
    re.compile(pattern.regex) for pattern in ItalianPhoneRecognizer().patterns
)

ENTITY_PRIORITY = {
    "CLINICAL_IDENTIFIER": 100,
    "EPISODE_INFO": 95,
    "IT_FISCAL_CODE": 92,
    "IT_VAT_CODE": 90,
    "ADDRESS": 80,
    "PHONE_NUMBER": 70,
    "PERSON": 60,
    "ORGANIZATION": 50,
    "LOCATION": 40,
    "DATE_TIME": 30,
}


def resolve_results(
    results: list[RecognizerResult], text: str | None = None
) -> list[RecognizerResult]:
    """Keep valid, highest-priority non-overlapping entity spans."""
    ordered = sorted(
        results,
        key=lambda result: (
            -ENTITY_PRIORITY.get(result.entity_type, 0),
            -result.score,
            -(result.end - result.start),
            result.start,
        ),
    )
    selected: list[RecognizerResult] = []
    for result in ordered:
        if result.entity_type in SEMANTIC_ENTITY_TYPES and result.score < MIN_SEMANTIC_SCORE:
            continue
        if (
            text is not None
            and result.entity_type == "PHONE_NUMBER"
            and result.score < MIN_PHONE_SCORE
            and not any(
                pattern.fullmatch(text[result.start : result.end])
                for pattern in ITALIAN_PHONE_PATTERNS
            )
        ):
            continue
        if result.start >= result.end:
            continue
        if any(result.start < other.end and other.start < result.end for other in selected):
            continue
        selected.append(result)
    return sorted(selected, key=lambda result: result.start)


def anonymize_results(text: str, results: list[RecognizerResult]) -> str:
    """Replace selected entity spans from right to left."""
    anonymized = text
    for result in sorted(results, key=lambda item: item.start, reverse=True):
        anonymized = (
            anonymized[: result.start] + f"<{result.entity_type}>" + anonymized[result.end :]
        )
    return anonymized
