from presidio_analyzer import Pattern, PatternRecognizer


class ClinicalIdentifierRecognizer(PatternRecognizer):
    """Recognizes structured Italian clinical identifiers."""

    def __init__(self) -> None:
        super().__init__(
            supported_entity="CLINICAL_IDENTIFIER",
            patterns=[
                Pattern(
                    name="patient_id",
                    regex=r"(?<![A-Z0-9])PAT-[0-9]{4}-[0-9]{6}(?![A-Z0-9])",
                    score=0.99,
                ),
                Pattern(
                    name="health_policy",
                    regex=r"(?<![A-Z0-9])PRIV-IT-[0-9]{4}-[0-9]{6}(?![A-Z0-9])",
                    score=0.99,
                ),
                Pattern(
                    name="clinical_protocol",
                    regex=r"(?<![A-Z0-9])CI-[0-9]{4}-[0-9]{6}(?![A-Z0-9])",
                    score=0.99,
                ),
                Pattern(
                    name="health_card",
                    regex=r"(?<![0-9])[0-9]{16}(?![0-9])",
                    score=0.85,
                ),
            ],
            context=["paziente", "tessera sanitaria", "polizza", "protocollo"],
            supported_language="it",
        )


class EpisodeInfoRecognizer(PatternRecognizer):
    """Recognizes medical record numbers used for clinical episodes."""

    def __init__(self) -> None:
        super().__init__(
            supported_entity="EPISODE_INFO",
            patterns=[
                Pattern(
                    name="medical_record_number",
                    regex=r"(?i)(?<=numero cartella )(?:\d{10}|\d{12})(?!\d)",
                    score=0.95,
                ),
                Pattern(
                    name="medical_record_number_colon",
                    regex=r"(?i)(?<=numero cartella: )(?:\d{10}|\d{12})(?!\d)",
                    score=0.95,
                ),
            ],
            context=["cartella", "episodio", "ricovero", "paziente"],
            supported_language="it",
        )
