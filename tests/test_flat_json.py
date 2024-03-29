import os
from gendiff.diff_generator import generate_diff


def test_normal_case():
    with open('tests/fixtures/flat_file_expected', 'r') as f:
        expected = f.read()
        assert generate_diff(
            'tests/fixtures/flat_file1.json',
            'tests/fixtures/flat_file2.json',
            'stylish',
        ) == expected


def test_single_empty_case():
    with open('tests/fixtures/flat_file_empty_expected', 'r') as f:
        expected = f.read()
        assert generate_diff(
            'tests/fixtures/flat_file1.json',
            'tests/fixtures/flat_file2_empty.json',
            'stylish',
        ) == expected


def test_both_empty_case():
    assert generate_diff(
        'tests/fixtures/flat_file2_empty.json',
        'tests/fixtures/flat_file2_empty.json',
        'stylish',
    ) == '{\n}'


def test_abs_path():
    with open('tests/fixtures/flat_file_expected', 'r') as f:
        expected = f.read()
        file1_abs_path = os.path.abspath('tests/fixtures/flat_file1.json')
        file2_abs_path = os.path.abspath('tests/fixtures/flat_file2.json')
        assert generate_diff(
            file1_abs_path,
            file2_abs_path,
            'stylish',
        ) == expected
