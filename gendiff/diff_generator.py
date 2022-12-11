from gendiff import diff_builder
from gendiff.file_reader import read_file
from gendiff.file_parser import parse_file
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
    files = map(read_file, (first_file_path, second_file_path))
    parsed_collections = map(parse_file, files)
    difference = diff_builder.dict_diff(parsed_collections)
    diff_out = diff_output(difference, format)
    return diff_out
