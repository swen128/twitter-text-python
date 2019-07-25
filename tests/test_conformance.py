from typing import List

import pytest

from src.parse_tweet import parse_tweet
from src.extract_urls import extract_urls, extract_urls_with_indices
from tests.utils import read_yaml

extract = read_yaml('tests/cases/extract.yml')['tests']
tlds = read_yaml('tests/cases/tlds.yml')['tests']
validate = read_yaml('tests/cases/validate.yml')['tests']


def get_table(test_cases: dict, group_name: str) -> List[list]:
    return [list(case.values()) for case in test_cases[group_name]]


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(extract, 'tco_urls_with_params')
)
def test_extract_tco_urls_with_params(description: str, text: str, expected: List[str]):
    assert extract_urls(text) == expected


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(extract, 'urls')
)
def test_extract_urls(description: str, text: str, expected: List[str]):
    assert extract_urls(text) == expected


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(tlds, 'country')
)
def test_tlds_country(description: str, text: str, expected: List[str]):
    assert extract_urls(text) == expected


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(extract, 'urls_with_indices')
)
def test_extract_urls_with_indices(description: str, text: str, expected: dict):
    assert extract_urls_with_indices(text) == expected


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(extract, 'urls_with_directional_markers')
)
def test_extract_urls_with_directional_markers(description: str, text: str, expected: dict):
    assert extract_urls_with_indices(text) == expected


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(validate, 'WeightedTweetsWithDiscountedEmojiCounterTest')
)
def test_validate_weighted_tweets_with_discounted_emoji_counter_test(description: str, text: str, expected: dict):
    assert parse_tweet(text)['weightedLength'] == expected['weightedLength']


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(validate, 'UnicodeDirectionalMarkerCounterTest')
)
def test_validate_unicode_directional_marker_counter_test(description: str, text: str, expected: dict):
    assert parse_tweet(text) == expected
