import json
import yaml


def dump(word, extention):
    if extention == '.json':
        dumped = json.dumps(word).strip('"')
    if extention == '.yml' or extention == '.yaml':
        dumped = yaml.dump(word).strip('...\n')
    return dumped
