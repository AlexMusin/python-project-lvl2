def get_name(inp_diff):
    return inp_diff['name']


def get_status(inp_diff):
    return inp_diff['status']


def get_all_values(inp_diff):
    '''Return all existing values'''
    if inp_diff['status'] == 'modified':
        raise Exception(
            '''Modified dictionaries have no values!'''
        )
    return inp_diff['values']


def get_init_value(inp_diff):
    if inp_diff['status'] == 'modified':
        raise Exception(
            '''Modified dictionaries have no values!'''
        )
    return inp_diff['values'][0]


def get_new_value(inp_diff):
    if inp_diff['status'] == 'modified':
        raise Exception(
            '''Modified dictionaries have no values!'''
        )
    if inp_diff['status'] != 'changed':
        raise Exception(
            '''This element was not changed.
            There is no new value!'''
        )
    return inp_diff['values'][1]


def get_children(inp_diff):
    if inp_diff['status'] != 'modified':
        raise Exception(
            '''This element was not dict.
            There is no children!'''
        )
    return inp_diff['children']
