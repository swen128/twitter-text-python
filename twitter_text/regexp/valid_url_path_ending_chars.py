import re

from .cyrillic_letters_and_marks import cyrillic_letters_and_marks
from .latin_accent_chars import latin_accent_chars
from .valid_url_balanced_parens import valid_url_balanced_parens
from ..regex_supplant import regex_supplant

valid_url_path_ending_chars = regex_supplant(
    re.compile(
        r'[\+\-a-z#{cyrillic_letters_and_marks}0-9=_#\/#{latin_accent_chars}]|(?:#{valid_url_balanced_parens})',
        re.IGNORECASE
    ),
    {
        'cyrillic_letters_and_marks': cyrillic_letters_and_marks,
        'latin_accent_chars': latin_accent_chars,
        'valid_url_balanced_parens': valid_url_balanced_parens
    }
)
