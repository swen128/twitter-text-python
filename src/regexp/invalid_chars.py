from .invalid_chars_group import invalid_chars_group
from ..regex_supplant import regex_supplant

invalid_chars = regex_supplant(
    r'[#{invalid_chars_group}]',
    {'invalid_chars_group': invalid_chars_group}
)
