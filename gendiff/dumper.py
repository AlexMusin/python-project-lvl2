import json
import yaml


FORMAT_LIST = ['.json', '.yaml', '.yml']
JSON = FORMAT_LIST[0]
YAML = FORMAT_LIST[1]
YML = FORMAT_LIST[2]


def dump(word, extention='.json'):
    '''Return value converted JSON or YAML
    regarding input extention'''
    if extention == JSON:
        dumped = json.dumps(word).strip('"')
    if extention == YML or extention == YAML:
        dumped = yaml.dump(word).strip('...\n')
    return dumped
