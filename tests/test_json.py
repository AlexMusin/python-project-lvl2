from gendiff.scripts.gendiff import generate_diff

def test_normal_case():
    with open('tests/fixtures/file_expected_format_stylish', 'r') as f:
        expected = f.read()
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json'
            ) == expected


def test_single_empty_case():
    with open(
        'tests/fixtures/file_empty_expected_format_stylish',
        'r'
        ) as f:
        expected = f.read()        
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/flat_file2_empty.json'
            ) == expected