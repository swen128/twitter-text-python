import re
import unicodedata
from dataclasses import dataclass, asdict
from math import floor
from typing import List, Dict

from .config import config
from .extract_emojis import extract_emojis_with_indices
from .extract_urls import extract_urls_with_indices
from .get_character_weight import get_character_weight
from .has_invalid_characters import has_invalid_characters


@dataclass(frozen=True)
class ParsedResult:
    valid: bool
    weightedLength: int
    permillage: int
    validRangeStart: int
    validRangeEnd: int
    displayRangeStart: int
    displayRangeEnd: int

    def asdict(self) -> dict:
        return asdict(self)


def convert_line_ending(string, to="\n"):
    return re.sub(r'\r\n|\r|\n', to, string)


def parse_tweet(text: str, options: dict = config['defaults']) -> ParsedResult:
    """
    Parse a Twitter text according to https://developer.twitter.com/en/docs/developer-utilities/twitter-text

    :param str text: A text to parse.
    :param dict options: Parameters for counting the weighted tweet length. This must have the following properties:

        max_weighted_tweet_length (int)
            Valid tweet messages must not exceed this weighted length.

        default_weight (int)
            Default weight to cover code points not defined in the ``ranges``.

        ranges (list of dict)
            A list of Unicode code point ranges, with a weight associated with each of these ranges.
            Each element of ``ranges`` must have the following attributes:

                - start (int)
                - end (int)
                - weight (int)

        scale (int)
            The weights are divided by ``scale``.

        emoji_parsing_enabled (bool)
            When set to ``True``, it counts an emoji consisting of multiple Unicode code points as a single character,
            resulting in a visually intuitive weighted length.

        transformed_url_length (int)
            The default length assigned to all URLs.

    :return ParsedResult: An object having the following properties:

        weightedLength (int)
            The weighted length of the twitter text.

            Each Unicode character (or URL, emoji) in ``text`` is assigned an integer weight,
            which is summed over to calculate `weightedLength`.

        valid (bool)
            True if the ``text`` is valid, i.e.,

            - ``weightedLength <= max_weighted_tweet_length``
            - ``text`` does not contain invalid characters.

        permillage (int)
            Equals to ``weightedLength // max_weighted_tweet_length * 1000``.

        displayRangeStart (int)
            Always 0.

        displayRangeEnd (int)
            Number of UTF-16 code units in ``text``, subtracted by one.

        validRangeStart (int)
            Always 0.

        validRangeEnd (int)
            Number of UTF-16 code units in the valid part of ``text``, subtracted by one.

            The "valid part" here means the longest valid Unicode substring starting from the leftmost of ``text``.


    Example:

    >>> parse_tweet('english text 日本語 😷 https://example.com')
    ParsedResult(
        weightedLength=46,
        valid=True,
        permillage=164,
        validRangeStart=0,
        validRangeEnd=38,
        displayRangeStart=0,
        displayRangeEnd=38
    )
    """
    scale = options['scale']
    transformed_url_length = options['transformed_url_length']
    default_weight = options['default_weight']
    emoji_parsing_enabled = options['emoji_parsing_enabled']
    max_weighted_tweet_length = options['max_weighted_tweet_length']

    normalized_text = convert_line_ending(unicodedata.normalize('NFC', text))

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
            weighted_length += default_weight
            char_index += len(emoji) - 1
        else:
            weighted_length += get_character_weight(normalized_text[char_index], options)

        if valid:
            valid = not has_invalid_characters(normalized_text[char_index:char_index + 1])

        if valid and weighted_length <= max_weighted_tweet_length * scale:
            valid_display_index = char_index

        char_index += 1

    weighted_length = int(weighted_length / scale)
    valid_display_offset = count_utf16_bytes(normalized_text[:valid_display_index + 1]) - 1
    normalization_offset = count_utf16_bytes(text) - count_utf16_bytes(normalized_text)

    return ParsedResult(
        weightedLength=weighted_length,
        valid=valid and 0 < weighted_length <= max_weighted_tweet_length,
        permillage=floor((weighted_length / max_weighted_tweet_length) * 1000),
        validRangeStart=0,
        validRangeEnd=valid_display_offset + normalization_offset,
        displayRangeStart=0,
        displayRangeEnd=count_utf16_bytes(text) - 1 if count_utf16_bytes(text) > 0 else 0
    )


def transform_entities_to_hash(entities: List[dict]) -> Dict[int, dict]:
    return {entity['indices'][0]: entity for entity in entities}


def count_utf16_bytes(text: str) -> int:
    return len(text.encode('utf-16')) // 2 - 1
