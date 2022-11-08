from gendiff.scripts.diff_builder import make_diff


def test_normal_case():
    with open('tests/fixtures/file_expected_diff_normal.txt') as f:
        expected = f.read()
        assert str(make_diff(
            'tests/fixtures/file1_smaller.json',
            'tests/fixtures/file2_smaller.json'
        )) == expected
