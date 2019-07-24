from typing import List

import pytest

from src.extract_urls import extract_urls, extract_urls_with_indices
from tests.utils import read_yaml

extract = read_yaml('tests/cases/extract.yml')['tests']


def get_table(test_cases: dict, group_name: str) -> List[list]:
    return [list(case.values()) for case in test_cases[group_name]]


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(extract, 'tco_urls_with_params')
)
def test_extract_tco_urls_with_params(description: str, text: str, expected: dict):
    assert extract_urls(text) == expected


@pytest.mark.parametrize(
    'description,text,expected',
    get_table(extract, 'urls')
)
def test_extract_urls(description: str, text: str, expected: dict):
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
