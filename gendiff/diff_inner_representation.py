NESTED = 'nested'
SAVED = 'saved'
DELETED = 'deleted'
ADDED = 'added'
CHANGED = 'changed'
NODE_TYPE = 'node_type'
VALUES = 'values'
NAME = 'name'


def get_name(inp_diff):
    '''Return name'''
    return inp_diff[NAME]


def get_node_type(inp_diff):
    '''Return node_type'''
    return inp_diff[NODE_TYPE]


def get_all_values(inp_diff):
    '''Return all existing values'''
    if inp_diff[NODE_TYPE] == NESTED:
        raise Exception(
            '''Nested dictionaries have no values!'''
        )
    return inp_diff[VALUES]


def get_init_value(inp_diff):
    '''Return initial value'''
    if inp_diff[NODE_TYPE] == NESTED:
        raise Exception(
            '''Nested dictionaries have no values!'''
        )
    return inp_diff[VALUES][0]


def get_new_value(inp_diff):
    '''Return new value'''
    if inp_diff[NODE_TYPE] == NESTED:
        raise Exception(
            '''Nested dictionaries have no values!'''
        )
    if inp_diff[NODE_TYPE] != CHANGED:
        raise Exception(
            '''This element was not changed.
            There is no new value!'''
        )
    return inp_diff[VALUES][1]


def get_children(inp_diff):
    '''Return children of nested node of input'''
    if inp_diff[NODE_TYPE] != NESTED:
        raise Exception(
            '''This node is not dict.
            There is no children!'''
        )
    return inp_diff['children']
