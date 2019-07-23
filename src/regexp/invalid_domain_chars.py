from .directional_markers_group import directional_markers_group
from .invalid_chars_group import invalid_chars_group
from .punct import punct
from .spaces_group import spaces_group
from ..regex_supplant import regex_supplant

invalid_domain_chars = regex_supplant(
    r'#{punct}#{spaces_group}#{invalid_chars_group}#{directional_markers_group}',
    {
        'punct': punct,
        'spaces_group': spaces_group,
        'invalid_chars_group': invalid_chars_group,
        'directional_markers_group': directional_markers_group
    }
)
