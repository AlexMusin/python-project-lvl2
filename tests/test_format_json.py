from gendiff.diff_generator import generate_diff
import json


def test_normal_case():
    with open('tests/fixtures/file_expected_format_json', 'r') as f:
        expected = f.read()
        diff = generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'json',
        )
        diff = sort_diff(json.loads(diff))
        expected = sort_diff(json.loads(expected))
        assert diff == expected

def sort_diff(diff):
    diff.sort(key=lambda k: k['name'])
    for elem in diff:
        if elem['node_type'] == 'nested':
            sort_diff(elem['children'])
    return diff
