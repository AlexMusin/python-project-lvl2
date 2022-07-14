import json
import yaml
from yaml.loader import SafeLoader


def parse(file_path, extention):
    with open(file_path, 'r') as f:
        if extention == '.json':
            parsed = json.load(f)
        if extention == '.yml' or extention == '.yaml':
            parsed = yaml.load(f, Loader=SafeLoader)
        if parsed is None:
            parsed = {}
    return parsed
