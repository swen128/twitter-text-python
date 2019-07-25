import re

from .cyrillic_letters_and_marks import cyrillic_letters_and_marks
from .latin_accent_chars import latin_accent_chars
from ..regex_supplant import regex_supplant

valid_general_url_path_chars = regex_supplant(
    re.compile(
        r"[a-z#{cyrillic_letters_and_marks}0-9!\*';:=\+,\.\$\/%#\[\]\-\u2013_~@\|&#{latin_accent_chars}]",
        re.IGNORECASE
    ),
    {
        'cyrillic_letters_and_marks': cyrillic_letters_and_marks,
        'latin_accent_chars': latin_accent_chars
    }
)
