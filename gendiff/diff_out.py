from gendiff.formatters.diff_out_plain import out as plain
from gendiff.formatters.diff_out_stylish import out as stylish
from gendiff.formatters.diff_out_json import out as json


FORMAT_STYLES = [
    'stylish',
    'plain',
    'json',
]

STYLISH = FORMAT_STYLES[0]
PLAIN = FORMAT_STYLES[1]
JSON = FORMAT_STYLES[2]


def validate_format(format):
    if format not in FORMAT_STYLES:
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


def diff_output(diff, format):
    validate_format(format)
    if format == STYLISH:
        return stylish(diff)
    if format == PLAIN:
        return plain(diff)
    if format == JSON:
        return json(diff)
