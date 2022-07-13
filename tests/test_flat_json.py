import pytest
from gendiff.scripts.gendiff import generate_diff


def test_normal_case():
    with open('tests/fixtures/flat_file_expected', 'r') as f:
        expected = f.read()
        assert generate_diff(
            'tests/fixtures/flat_file1.json',
            'tests/fixtures/flat_file2.json'
            ) == expected

def test_single_empty_case():
    with open(
        'tests/fixtures/flat_file_empty_expected',
        'r'
        ) as f:
        expected = f.read()        
        assert generate_diff(
            'tests/fixtures/flat_file1.json',
            'tests/fixtures/flat_file2_empty.json'
            ) == expected

def test_both_empty_case():
    assert generate_diff(
            'tests/fixtures/flat_file2_empty.json',
            'tests/fixtures/flat_file2_empty.json'
            ) == '{\n}'