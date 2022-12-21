from gendiff.diff_generator import generate_diff
from gendiff.diff_sort import sort_diff
import json


def test_normal_case():
    with open('tests/fixtures/file_expected_format_json', 'r') as f:
        expected = f.read()
        diff = generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'json',
        )
        diff = sort_diff(json.loads(diff))
        expected = sort_diff(json.loads(expected))
        assert diff == expected
