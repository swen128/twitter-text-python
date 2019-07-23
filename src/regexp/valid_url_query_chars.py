import re

valid_url_query_chars = re.compile(r"[a-z0-9!?*'@();:&=+$/%#\[\]\-_.,~|]", re.IGNORECASE)
