import json
import yaml


def parse_file(text, format):
    '''Get file
    return parsed collection'''
    if format == 'json':
        parsed = json.loads(text)
    else:
        parsed = yaml.load(text, Loader=yaml.SafeLoader) or {}
    return parsed
