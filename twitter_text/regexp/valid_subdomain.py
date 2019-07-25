from .valid_domain_chars import valid_domain_chars
from ..regex_supplant import regex_supplant

valid_subdomain = regex_supplant(
    r'(?:(?:#{valid_domain_chars}(?:[_-]|#{valid_domain_chars})*)?#{valid_domain_chars}\.)',
    {
        'valid_domain_chars': valid_domain_chars
    }
)
