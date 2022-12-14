from gendiff.diff_builder import dict_diff
from gendiff.file_parser import parse_file
from gendiff.file_reader import read_file


def test_normal_case():
    with open('tests/fixtures/file_expected_diff_normal.txt') as f:
        expected = f.read()
        file1_tup = read_file('tests/fixtures/file1_smaller.json')
        file2_tup = read_file('tests/fixtures/file2_smaller.json')
        dict1 = parse_file(file1_tup)
        dict2 = parse_file(file2_tup)
        diff = dict_diff(dict1, dict2)
        assert str(diff) == expected
