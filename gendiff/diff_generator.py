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
    file1_tup = read_file(first_file_path)
    file2_tup = read_file(second_file_path)
    dict1 = parse_file(file1_tup)
    dict2 = parse_file(file2_tup)
    difference = diff_builder.dict_diff(dict1, dict2)
    diff_out = diff_output(difference, format)
    return diff_out
