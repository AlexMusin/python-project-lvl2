from gendiff import node_type


def get_name(inp_diff):
    '''Return name'''
    return inp_diff['name']


def get_node_type(inp_diff):
    '''Return node_type'''
    return inp_diff['node_type']


def get_all_values(inp_diff):
    '''Return all existing values'''
    if inp_diff['node_type'] == node_type.type()['nested']:
        raise Exception(
            '''Nested dictionaries have no values!'''
        )
    return inp_diff['values']


def get_init_value(inp_diff):
    '''Return initial value'''
    if inp_diff['node_type'] == node_type.type()['nested']:
        raise Exception(
            '''Nested dictionaries have no values!'''
        )
    return inp_diff['values'][0]


def get_new_value(inp_diff):
    '''Return new value'''
    if inp_diff['node_type'] == node_type.type()['nested']:
        raise Exception(
            '''Nested dictionaries have no values!'''
        )
    if inp_diff['node_type'] != node_type.type()['changed']:
        raise Exception(
            '''This element was not changed.
            There is no new value!'''
        )
    return inp_diff['values'][1]


def get_children(inp_diff):
    '''Return children of nested node of input'''
    if inp_diff['node_type'] != node_type.type()['nested']:
        raise Exception(
            '''This node is not dict.
            There is no children!'''
        )
    return inp_diff['children']
