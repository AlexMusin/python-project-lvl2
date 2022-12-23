from gendiff import diff_builder
from gendiff.file_reader import read_file
from gendiff.file_parser import parse_file
from gendiff.diff_out import diff_output


DEFAULT_FORMAT = 'stylish'


def generate_diff(first_file_path, second_file_path, format=DEFAULT_FORMAT):
    text1, format1 = read_file(first_file_path)
    text2, format2 = read_file(second_file_path)
    dict1 = parse_file(text1, format1)
    dict2 = parse_file(text2, format2)
    difference = diff_builder.dict_diff(dict1, dict2)
    diff_out = diff_output(difference, format)
    return diff_out
