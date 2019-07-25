import unicodedata
from math import floor
from typing import List, Dict

from .config import config
from .extract_emojis import extract_emojis_with_indices
from .extract_urls import extract_urls_with_indices
from .get_character_weight import get_character_weight
from .has_invalid_characters import has_invalid_characters


def parse_tweet(text: str, options: dict = config['defaults']) -> dict:
    scale = options['scale']
    transformed_url_length = options['transformed_url_length']
    emoji_parsing_enabled = options['emoji_parsing_enabled']
    max_weighted_tweet_length = options['max_weighted_tweet_length']

    normalized_text = unicodedata.normalize('NFC', text)

    url_entities_map = transform_entities_to_hash(extract_urls_with_indices(normalized_text))
    emoji_entities_map = transform_entities_to_hash(extract_emojis_with_indices(normalized_text))

    weighted_length = 0
    valid_display_index = 0
    valid = True
    char_index = 0

    while char_index < len(normalized_text):
        if char_index in url_entities_map:
            url = url_entities_map[char_index]['url']
            weighted_length += transformed_url_length * scale
            char_index += len(url) - 1
        elif emoji_parsing_enabled and char_index in emoji_entities_map:
            emoji = emoji_entities_map[char_index]['emoji']
            weighted_length += get_character_weight(emoji[0], options)
            char_index += len(emoji) - 1
        else:
            weighted_length += get_character_weight(normalized_text[char_index], options)

        if valid:
            valid = not has_invalid_characters(normalized_text[char_index:char_index + 1])

        if valid and weighted_length <= max_weighted_tweet_length * scale:
            valid_display_index = char_index

        char_index += 1

    weighted_length = int(weighted_length / scale)
    normalization_offset = len(text) - len(normalized_text)

    return {
        'weightedLength': weighted_length,
        'valid': valid and 0 < weighted_length <= max_weighted_tweet_length,
        'permillage': floor((weighted_length / max_weighted_tweet_length) * 1000),
        'validRangeStart': 0,
        'validRangeEnd': valid_display_index + normalization_offset,
        'displayRangeStart': 0,
        'displayRangeEnd': len(text) - 1 if len(text) > 0 else 0
    }


def transform_entities_to_hash(entities: List[dict]) -> Dict[int, dict]:
    return {entity['indices'][0]: entity for entity in entities}


