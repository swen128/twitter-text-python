import re

invalid_url_without_protocol_preceding_chars = re.compile(r'[-_./]$')
