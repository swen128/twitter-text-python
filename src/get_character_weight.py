def get_character_weight(char: str, options: dict) -> int:
    """
    Return an integer weight corresponding to `char`.
    The weight is determined by the Unicode code point of `char` and ranges specified by `options`.

    >>> char = '日'
    >>> options = {
    ...     'default_weight': 200,
    ...     'ranges': [
    ...         { 'start': 0, 'end': 4351, 'weight': 100 },
    ...         { 'start': 8192, 'end': 8205, 'weight': 100 }
    ...     ]
    >>> get_character_weight(char, options)
    200
    """
    ranges = options['ranges']
    char_code_point = ord(char[0])
    match = [range['weight'] for range in ranges if range['start'] <= char_code_point <= range['end']]
    weight = match[0] if match != [] else options['default_weight']

    return weight
