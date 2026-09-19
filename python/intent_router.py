"""Simple deterministic intent router for educational use."""

RULES = {
    "billing": ("invoice", "payment", "refund", "charge"),
    "technical_support": ("error", "bug", "not working", "failed"),
    "sales": ("price", "plan", "pricing", "buy"),
}


def classify(message: str) -> tuple[str, float]:
    text = message.lower().strip()
    if not text:
        return "unknown", 0.0

    for intent, keywords in RULES.items():
        matches = sum(1 for keyword in keywords if keyword in text)
        if matches:
            return intent, min(1.0, 0.5 + matches * 0.15)

    return "unknown", 0.0


if __name__ == "__main__":
    import sys

    message = " ".join(sys.argv[1:]) or "hello"
    print(classify(message))
