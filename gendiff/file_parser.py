import json
import yaml


FORMAT_LIST = ['.json', '.yaml', '.yml']
JSON = FORMAT_LIST[0]


def validate_file_format(format):
    if format not in FORMAT_LIST:
        raise Exception('Wrong file format!')


def parse_file(text, format):
    '''Get file
    Check file format
    Return parsed collection'''
    validate_file_format(format)
    if format == JSON:
        parsed = json.loads(text)
    else:
        parsed = yaml.load(text, Loader=yaml.SafeLoader) or {}
    return parsed
