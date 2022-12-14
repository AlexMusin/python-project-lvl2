from gendiff import diff_builder
from gendiff.file_reader import read_file
from gendiff.file_parser import parse_file
from gendiff.diff_out import diff_output


FORMAT_TUP = (
    'stylish',
    'plain',
    'json',
)


def generate_diff(first_file_path, second_file_path, format='stylish'):
    files = map(read_file, (first_file_path, second_file_path))
    parsed_collections = map(parse_file, files)
    difference = diff_builder.dict_diff(parsed_collections)
    diff_out = diff_output(difference, format)
    return diff_out
