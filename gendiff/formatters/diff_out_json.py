import json
from gendiff import diff_inner_representation as ig


def out(inp_diff):
    '''Return difference in JSON format with indentation'''
    out = json.dumps(inp_diff, indent=2)
    return out
