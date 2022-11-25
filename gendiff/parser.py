from distutils import extension
import json
import yaml


def parse_file(file_tup):
    '''Get file 
    return parsed collection'''
    file, extention = file_tup
    if extention == 'json':
        parsed = json.loads(file)
    else:
        parsed = yaml.load(file, Loader=yaml.SafeLoader) or {}
    return parsed
