import json
import yaml


FORMAT_LIST = ['.json', '.yaml', '.yml']


def validate_file_format(format):
    if format not in FORMAT_LIST:
        raise Exception('Wrong file format!')


def parse_file(text, format):
    '''Get file
    Check file format
    Return parsed collection'''
    validate_file_format(format)
    if format == 'json':
        parsed = json.loads(text)
    else:
        parsed = yaml.load(text, Loader=yaml.SafeLoader) or {}
    return parsed
