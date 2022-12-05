from gendiff.diff_builder import dict_diff
from gendiff.files_parser import parse_files
from gendiff.files_input import read_files


def test_normal_case():
    with open('tests/fixtures/file_expected_diff_normal.txt') as f:
        expected = f.read()
        files_read = read_files('tests/fixtures/file1_smaller.json', 'tests/fixtures/file2_smaller.json')
        #print(files_read)
        files_parsed = parse_files(files_read)
        diff = dict_diff(files_parsed)
        assert str(diff) == expected
