from gendiff.scripts import diff_builder
from gendiff.scripts import diff_out_plain
from gendiff.scripts import diff_out_stylish
from gendiff.scripts import diff_out_json


def generate_diff(first_file_path, second_file_path, format='stylish'):
    '''Launch difference building and output with defined format'''
    if format == 'stylish':
        return diff_out_stylish.out_stylish(
            diff_builder.make_diff(
                first_file_path,
                second_file_path,
            )
        )
    if format == 'plain':
        return diff_out_plain.out_plain(
            diff_builder.make_diff(
                first_file_path,
                second_file_path,
            )
        )
    if format == 'json':
        return diff_out_json.out_json(
            diff_builder.make_diff(
                first_file_path,
                second_file_path,
            )
        )
