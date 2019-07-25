import re
from .valid_domain import valid_domain
from .valid_url_query_chars import valid_url_query_chars
from .valid_url_query_ending_chars import valid_url_query_ending_chars
from .valid_port_number import valid_port_number
from .valid_url_path import valid_url_path
from .valid_url_preceding_chars import valid_url_preceding_chars
from ..regex_supplant import regex_supplant

extract_url = regex_supplant(
    '(' +  # $1 total match
    '(#{valid_url_preceding_chars})' +  # $2 Preceding character
    '(' +  # $3 URL
    '(https?:\\/\\/)?' +  # $4 Protocol (optional)
    '(#{valid_domain})' +  # $5 Domain(s)
    '(?::(#{valid_port_number}))?' +  # $6 Port number (optional)
    '(\\/#{valid_url_path}*)?' +  # $7 URL Path
    '(\\?#{valid_url_query_chars}*#{valid_url_query_ending_chars})?' +  # $8 Query String
    ')' +
    ')',
    {
        'valid_domain': valid_domain,
        'valid_url_query_chars': valid_url_query_chars,
        'valid_url_query_ending_chars': valid_url_query_ending_chars,
        'valid_port_number': valid_port_number,
        'valid_url_path': valid_url_path,
        'valid_url_preceding_chars': valid_url_preceding_chars
    },
    re.IGNORECASE
)
