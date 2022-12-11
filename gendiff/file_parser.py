import json
import yaml


def parse_file(file_tup):
    '''Get file
    return parsed collection'''
    text, format = file_tup
    if format == 'json':
        parsed = json.loads(text)
    else:
        parsed = yaml.load(text, Loader=yaml.SafeLoader) or {}
    return parsed
