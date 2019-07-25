import re

from .valid_general_url_path_chars import valid_general_url_path_chars
from ..regex_supplant import regex_supplant

valid_url_balanced_parens = regex_supplant(
    '\\(' +
    '(?:' +
    '#{valid_general_url_path_chars}+' +
    '|' +
    # allow one nested level of balanced parentheses
    '(?:' +
    '#{valid_general_url_path_chars}*' +
    '\\(' +
    '#{valid_general_url_path_chars}+' +
    '\\)' +
    '#{valid_general_url_path_chars}*' +
    ')' +
    ')' +
    '\\)',
    {
        'valid_general_url_path_chars': valid_general_url_path_chars
    },
    re.IGNORECASE
)
