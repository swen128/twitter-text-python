from typing import List, Tuple

import pytest
import yaml

from twitter_text import parse_tweet, extract_urls, extract_urls_with_indices


def read_yaml(path) -> dict:
    with open(path, mode='r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_table(test_cases: dict, group_name: str) -> Tuple[str, List[list]]:
    header = ",".join(test_cases[group_name][0].keys())
    values = [list(case.values()) for case in test_cases[group_name]]
    return header, values


def parametrize(test_cases: dict, group_name: str):
    return pytest.mark.parametrize(*get_table(test_cases, group_name))


extract = read_yaml('tests/cases/extract.yml')['tests']
tlds = read_yaml('tests/cases/tlds.yml')['tests']
validate = read_yaml('tests/cases/validate.yml')['tests']


@parametrize(extract, 'tco_urls_with_params')
def test_extract_tco_urls_with_params(description: str, text: str, expected: List[str]):
    assert extract_urls(text) == expected


@parametrize(extract, 'urls')
def test_extract_urls(description: str, text: str, expected: List[str]):
    assert extract_urls(text) == expected


@parametrize(tlds, 'country')
def test_tlds_country(description: str, text: str, expected: List[str]):
    assert extract_urls(text) == expected


@parametrize(extract, 'urls_with_indices')
def test_extract_urls_with_indices(description: str, text: str, expected: dict):
    assert extract_urls_with_indices(text) == expected


@parametrize(extract, 'urls_with_directional_markers')
def test_extract_urls_with_directional_markers(description: str, text: str, expected: dict):
    assert extract_urls_with_indices(text) == expected


@parametrize(validate, 'WeightedTweetsWithDiscountedEmojiCounterTest')
def test_validate_weighted_tweets_with_discounted_emoji_counter_test(description: str, text: str, expected: dict):
    assert parse_tweet(text).asdict() == expected


@parametrize(validate, 'UnicodeDirectionalMarkerCounterTest')
def test_validate_unicode_directional_marker_counter_test(description: str, text: str, expected: dict):
    assert parse_tweet(text).asdict() == expected
