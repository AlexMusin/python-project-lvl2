from gendiff.formatters.diff_out_plain import out as plain
from gendiff.formatters.diff_out_stylish import out as stylish
from gendiff.formatters.diff_out_json import out as json


FORMAT_STYLES = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def validate_format(format):
    if format not in FORMAT_STYLES.keys():
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
    return FORMAT_STYLES[format](diff)
