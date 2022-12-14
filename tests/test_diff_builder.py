from gendiff.diff_builder import dict_diff
from gendiff.file_parser import parse_file
from gendiff.file_reader import read_file


def test_normal_case():
    with open('tests/fixtures/file_expected_diff_normal.txt') as f:
        expected = f.read()
        text1, format1 = read_file('tests/fixtures/file1_smaller.json')
        text2, format2 = read_file('tests/fixtures/file2_smaller.json')
        dict1 = parse_file(text1, format1)
        dict2 = parse_file(text2, format2)
        diff = dict_diff(dict1, dict2)
        assert str(diff) == expected
