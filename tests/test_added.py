from typing import List, Tuple

import pytest
import yaml

from twitter_text import parse_tweet, extract_urls_with_indices


def read_yaml(path) -> dict:
    with open(path, mode='r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_table(test_cases: dict, group_name: str) -> Tuple[str, List[list]]:
    header = ",".join(test_cases[group_name][0].keys())
    values = [list(case.values()) for case in test_cases[group_name]]
    return header, values


def parametrize(test_cases: dict, group_name: str):
    return pytest.mark.parametrize(*get_table(test_cases, group_name))


added = read_yaml('tests/cases/added.yml')['tests']


@parametrize(added, 'ParseTweet')
def test_added_parse_tweet(description: str, text: str, expected: dict):
    assert parse_tweet(text).asdict() == expected


@parametrize(added, 'ExtractUrlsWithIndices')
def test_added_extract_urls_with_indices(description: str, text: str, expected: dict):
    assert extract_urls_with_indices(text) == expected
