from .valid_cctld import valid_cctld
from .valid_domain_name import valid_domain_name
from .valid_gtld import valid_gtld
from .valid_punycode import valid_punycode
from .valid_subdomain import valid_subdomain
from ..regex_supplant import regex_supplant

valid_domain = regex_supplant(
    r'(?:#{valid_subdomain}*#{valid_domain_name}(?:#{valid_gtld}|#{valid_cctld}|#{valid_punycode}))',
    {
        'valid_subdomain': valid_subdomain,
        'valid_domain_name': valid_domain_name,
        'valid_gtld': valid_gtld,
        'valid_cctld': valid_cctld,
        'valid_punycode': valid_punycode
    }
)
