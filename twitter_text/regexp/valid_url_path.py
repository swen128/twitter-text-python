import re

from .valid_general_url_path_chars import valid_general_url_path_chars
from .valid_url_balanced_parens import valid_url_balanced_parens
from .valid_url_path_ending_chars import valid_url_path_ending_chars
from ..regex_supplant import regex_supplant

valid_url_path = regex_supplant(
    '(?:' +
    '(?:' +
    '#{valid_general_url_path_chars}*' +
    '(?:#{valid_url_balanced_parens}#{valid_general_url_path_chars}*)*' +
    '#{valid_url_path_ending_chars}' +
    ')|(?:@#{valid_general_url_path_chars}+/)' +
    ')',
    {
        'valid_general_url_path_chars': valid_general_url_path_chars,
        'valid_url_balanced_parens': valid_url_balanced_parens,
        'valid_url_path_ending_chars': valid_url_path_ending_chars
    },
    re.IGNORECASE
)
