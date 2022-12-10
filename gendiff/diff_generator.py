from gendiff import diff_builder
from gendiff.files_input import read_files
from gendiff.files_parser import parse_files
from gendiff.diff_out import diff_output


FORMAT_TUP = (
    'stylish',
    'plain',
    'json',
)


def validate_format(format):
    if format not in FORMAT_TUP:
        raise Exception(
            '''
            Entered format is not valid
            Please choose one of formats below:
            - stylish
            - plain
            - json
            Default: stylish
            '''
        )


def generate_diff(first_file_path, second_file_path, format='stylish'):
    validate_format(format)
    files = read_files(first_file_path, second_file_path)
    parsed_files = parse_files(files)
    difference = diff_builder.dict_diff(parsed_files)
    diff_out = diff_output(difference, format)
    return diff_out
