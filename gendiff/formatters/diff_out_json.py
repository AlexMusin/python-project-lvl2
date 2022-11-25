import json


def out_json(inp_diff):
    '''Return difference in JSON format with indentation'''
    return json.dumps(inp_diff, indent=2)
