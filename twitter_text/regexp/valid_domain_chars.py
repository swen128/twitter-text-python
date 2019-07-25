from .invalid_domain_chars import invalid_domain_chars
from ..regex_supplant import regex_supplant

valid_domain_chars = regex_supplant(
    r'[^#{invalid_domain_chars}]',
    {
        'invalid_domain_chars': invalid_domain_chars
    }
)
