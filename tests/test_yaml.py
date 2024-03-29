from gendiff.diff_generator import generate_diff


def test_normal_case():
    with open('tests/fixtures/file_expected_format_stylish', 'r') as f:
        expected = f.read()
        assert generate_diff(
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            'stylish',
        ) == expected
