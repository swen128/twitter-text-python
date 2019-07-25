import re

from .latin_accent_chars import latin_accent_chars
from .valid_cctld import valid_cctld
from .valid_gtld import valid_gtld
from .valid_punycode import valid_punycode
from ..regex_supplant import regex_supplant

valid_ascii_domain = regex_supplant(
    re.compile(
        r'(?:(?:[\-a-z0-9#{latin_accent_chars}]+)\.)+(?:#{valid_gtld}|#{valid_cctld}|#{valid_punycode})',
        re.IGNORECASE
    ),
    {
        'latin_accent_chars': latin_accent_chars,
        'valid_gtld': valid_gtld,
        'valid_cctld': valid_cctld,
        'valid_punycode': valid_punycode
    }
)
