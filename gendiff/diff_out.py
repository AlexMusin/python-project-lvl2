from gendiff.formatters import diff_out_plain
from gendiff.formatters import diff_out_stylish
from gendiff.formatters import diff_out_json


def diff_output(diff, format):
    if format == 'stylish':
        return diff_out_stylish.out_stylish(diff)
    if format == 'plain':
        return diff_out_plain.out_plain(diff)
    if format == 'json':
        return diff_out_json.out_json(diff)
