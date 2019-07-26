from typing import List

from .regexp.emoji import emoji


def extract_emojis_with_indices(text: str) -> List[dict]:
    """
    Extract emojis present in ``text`` along with their Unicode code point indices.

    >>> extract_emojis_with_indices('text 😷')
    {'emoji': '😷', 'indices': [5, 6]}

    >>> extract_emojis_with_indices('🙋🏽👨‍🎤')
    [{'emoji': '🙋🏽', 'indices': [0, 2]}, {'emoji': '👨\u200d🎤', 'indices': [2, 5]}]
    """
    def generator():
        for match in emoji.finditer(text):
            yield {
                'emoji': match.group(0),
                'indices': [match.start(), match.end()]
            }

    return list(generator())
