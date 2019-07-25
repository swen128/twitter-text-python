from .regexp.invalid_chars import invalid_chars


def has_invalid_characters(text: str) -> bool:
    return invalid_chars.search(text) is not None
