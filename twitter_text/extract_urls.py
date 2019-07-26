from typing import List, Optional

from .regexp.extract_url import extract_url
from .regexp.invalid_url_without_protocol_preceding_chars import invalid_url_without_protocol_preceding_chars
from .regexp.valid_ascii_domain import valid_ascii_domain
from .regexp.valid_tco_url import valid_tco_url

default_protocol = 'https://'
max_url_length = 4096
max_tco_slug_length = 40


def extract_urls(text: str, extract_urls_without_protocol: bool = True) -> List[str]:
    """
    Extract valid URLs present in ``text``.

    >>> extract_urls('http://twitter.com/これは日本語です。example.com中国語')
    ["url": "http://twitter.com/", "example.com"]
    """
    return [dic['url'] for dic in extract_urls_with_indices(text, extract_urls_without_protocol)]


def extract_urls_with_indices(text: str, extract_urls_without_protocol: bool = True) -> List[dict]:
    """
    Extract valid URLs present in ``text`` along with their Unicode code point indices.

    >>> extract_urls_with_indices('http://twitter.com/これは日本語です。example.com中国語')
    [
        {
            "url": "http://twitter.com/",
            "indices": [0, 19]
        },
        {
            "url": "example.com",
            "indices": [28, 39]
        }
    ]
    """
    if text == '' or ('.' not in text if extract_urls_without_protocol else ':' not in text):
        return []

    urls = []

    for url_match in extract_url.finditer(text):
        _, before, url, protocol, domain, _, path, _ = url_match.groups()
        end_position = url_match.end()
        start_position = end_position - len(url)

        if not is_valid_url(url, protocol or default_protocol, domain):
            continue

        # extract ASCII-only domains.
        if protocol is None:
            if not extract_urls_without_protocol or \
                    invalid_url_without_protocol_preceding_chars.match(before):
                continue

            last_url = None
            for ascii_domain_match in valid_ascii_domain.finditer(domain):
                ascii_domain = ascii_domain_match.group(0)
                ascii_start_position = ascii_domain_match.start()
                ascii_end_position = ascii_domain_match.end()
                last_url = {
                    'url': ascii_domain,
                    'indices': [start_position + ascii_start_position, start_position + ascii_end_position]
                }
                urls.append(last_url)

            # no ASCII-only domain found. Skip the entire URL.
            if last_url is None:
                continue

            # lastUrl only contains domain. Need to add path and query if they exist.
            if path:
                last_url['url'] = url.replace(domain, last_url['url'])
                last_url['indices'][1] = end_position
        else:
            # In the case of t.co URLs, don't allow additional path characters.
            tco_url_match = valid_tco_url.search(url)

            if tco_url_match:
                tco_url_slug = tco_url_match.group(1)
                if tco_url_slug and len(tco_url_slug) > max_tco_slug_length:
                    continue
                else:
                    url = tco_url_match.group(0)
                    end_position = start_position + len(url)

            urls.append({
                'url': url,
                'indices': [start_position, end_position]
            })

    return urls


def is_valid_url(url: str, protocol: str, domain: str) -> bool:
    puny_encoded_domain = idna_to_ascii(domain)

    if (not puny_encoded_domain) or len(puny_encoded_domain) == 0:
        return False
    else:
        url_length = len(url) + len(puny_encoded_domain) - len(domain)
        return len(protocol) + url_length <= max_url_length


def idna_to_ascii(domain: str) -> Optional[str]:
    """
    Convert an Internationalized Domain Name (IDN) into a Punycode string.
    Return `None` if the `domain` is invalid.

    >>> idna_to_ascii('日本語.jp')
    'xn--wgv71a119e.jp'
    """
    try:
        return domain.encode('idna').decode('ascii')
    except Exception:
        return None
