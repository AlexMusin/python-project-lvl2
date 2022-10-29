import json
import yaml
from os import path


EXTENTIONS_LIST = ['.json', '.yaml', '.yml']


def parser(file_path):
    '''Get file path
    return parsed collection'''
    extention = path.splitext(file_path)[1]
    if extention not in EXTENTIONS_LIST:
        raise Exception('Wrong file extention!')
    with open(file_path, 'r') as f:
        if extention == 'json':
            parsed = json.loads(f)
        else:
            parsed = yaml.load(f, Loader=yaml.SafeLoader) or {}
    return parsed
