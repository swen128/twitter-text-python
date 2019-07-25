from typing import List

from .regexp.emoji import emoji


def extract_emojis_with_indices(text: str) -> List[dict]:
    def generator():
        for match in emoji.finditer(text):
            yield {
                'emoji': match.group(0),
                'indices': [match.start(), match.end()]
            }

    return list(generator())
