import re
from typing import Dict, Union, Pattern, Match


def regex_supplant(regex: Union[str, Pattern], dic: Dict[str, Union[str, Pattern]], flags=0) -> Pattern:
    def repl(match: Match) -> str:
        name = match.group(1)
        pattern = dic.get(name, '')
        return pattern if isinstance(pattern, str) else pattern.pattern

    regex_str = regex if isinstance(regex, str) else regex.pattern
    new_flags = flags if isinstance(regex, str) else regex.flags | flags
    assembled_pat = re.sub(r'#\{(\w+)\}', repl, regex_str)

    return re.compile(assembled_pat, new_flags)
