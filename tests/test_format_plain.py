from gendiff.diff_generator import generate_diff


def test_normal_case():
    with open('tests/fixtures/file_expected_format_plain', 'r') as f:
        expected = f.read()
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'plain',
        ) == expected
