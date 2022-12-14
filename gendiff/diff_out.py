from gendiff.formatters.diff_out_plain import out as plain
from gendiff.formatters.diff_out_stylish import out as stylish
from gendiff.formatters.diff_out_json import out as json


FORMAT_STYLES = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def diff_output(diff, format):
    return FORMAT_STYLES[format](diff)
