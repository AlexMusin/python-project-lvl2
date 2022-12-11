from gendiff.diff_builder import dict_diff
from gendiff.file_parser import parse_file
from gendiff.file_reader import read_file


def test_normal_case():
    with open('tests/fixtures/file_expected_diff_normal.txt') as f:
        expected = f.read()
        files_read = map(read_file, (
            'tests/fixtures/file1_smaller.json',
            'tests/fixtures/file2_smaller.json',
        )
        )
        files_parsed = map(parse_file, files_read)
        diff = dict_diff(files_parsed)
        assert str(diff) == expected
