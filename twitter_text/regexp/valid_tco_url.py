import re

from .valid_url_query_chars import valid_url_query_chars
from .valid_url_query_ending_chars import valid_url_query_ending_chars
from ..regex_supplant import regex_supplant

valid_tco_url = regex_supplant(
    r'^https?:\/\/t\.co\/([a-z0-9]+)(?:\?#{valid_url_query_chars}*#{valid_url_query_ending_chars})?',
    {
        'valid_url_query_chars': valid_url_query_chars,
        'valid_url_query_ending_chars': valid_url_query_ending_chars
    },
    re.IGNORECASE
)
