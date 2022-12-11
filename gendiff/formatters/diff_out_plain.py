import gendiff.diff_inner_representation as ig
from gendiff.dumper import dump


def out_plain(inp_diff):
    '''Build plain-style output'''
    out_list = [
        f'Property {elem[0]} was {elem[1]}'
        for elem in prepare_list(inp_diff)
    ]
    return '\n'.join(out_list)


def prepare_list(inp_diff):
    '''Make in-between list for difference output'''
    def recourse(item, path):
        node_type = ig.get_node_type(item)
        name = ig.get_name(item)
        path = ('.'.join([path, name])).strip('.')
        statement = []
        if node_type == 'saved':
            return []
        if node_type != 'modified':
            if node_type == 'deleted':
                statement = 'removed'
            if node_type == 'added':
                statement = (
                    f'added with value: '
                    f'{dump_values(ig.get_all_values(item))}'
                )
            if node_type == 'changed':
                statement = (
                    f'updated. From '
                    f'{dump_values(ig.get_init_value(item))} '
                    f'to {dump_values(ig.get_new_value(item))}'
                )
            return (dump_values(path), statement)
        elif node_type == 'modified':
            return (
                list(map(
                    lambda node: recourse(node, path),
                    ig.get_children(item)
                ))
            )
    return flatten(list(map(lambda x: recourse(x, path=''), inp_diff)))


def dump_values(value):
    '''JSON-format calue dumper'''
    if not isinstance(value, dict):
        if isinstance(value, str):
            return f"'{dump(value)}'"
        return dump(value)
    else:
        return '[complex value]'


def flatten(inp_list):
    '''Flatten list'''
    a = []

    def recourse(item):
        if not isinstance(item, list):
            a.append(item)
        else:
            list(map(recourse, item))
    recourse(inp_list)
    return a
