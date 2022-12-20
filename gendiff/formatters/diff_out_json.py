import json
from gendiff import diff_inner_representation as ig


def out(inp_diff):
    '''Return difference in JSON format with indentation'''
    sorted_diff = sorted(inp_diff, key=lambda k: ig.get_name(k))
    out = json.dumps(sorted_diff, indent=2)
    return out
