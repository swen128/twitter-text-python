from .directional_markers_group import directional_markers_group
from .invalid_chars_group import invalid_chars_group
from ..regex_supplant import regex_supplant

valid_url_preceding_chars = regex_supplant(
    r'(?:[^A-Za-z0-9@＠$#＃#{invalid_chars_group}]|[#{directional_markers_group}]|^)',
    {
        'invalid_chars_group': invalid_chars_group,
        'directional_markers_group': directional_markers_group
    }
)
