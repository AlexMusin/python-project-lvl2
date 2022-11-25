from gendiff.scripts import diff_builder
from gendiff.scripts.files_input import read_files
from gendiff.scripts.files_parser import parse_files
from gendiff.scripts.diff_out import diff_output


FORMAT_LIST = [
    'stylish',
    'plain',
    'json',
]


def generate_diff(first_file_path, second_file_path, format):
    '''Launch difference building and output with defined format'''
    if format not in FORMAT_LIST:
        print('''User defined format is not available. 
        Format switched to "stylish"''')
        format = 'stylish'
    files = read_files(first_file_path, second_file_path)
    parsed_files = parse_files(files)
    difference = diff_builder.dict_diff(parsed_files)
    diff_out = diff_output(difference, format)
    return diff_out
