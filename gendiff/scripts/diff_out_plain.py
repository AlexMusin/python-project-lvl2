import gendiff.scripts.diff_inner_representation as ig
from gendiff.scripts.dumper import dump


def out_plain(inp_diff):
    out_list = [
        f'Property {elem[0]} was {elem[1]}'
        for elem in prepare_list(inp_diff)
    ]
    return '\n'.join(out_list)


def prepare_list(inp_diff):
    def recourse(item, path):
        status = ig.get_status(item)
        name = ig.get_name(item)
        path = ('.'.join([path, name])).strip('.')
        statement = []
        if status == 'saved':
            return []
        if status != 'modified':
            if status == 'deleted':
                statement = 'removed'
            if status == 'added':
                statement = (
                    f'added with value: '
                    f'{dump_values(ig.get_all_values(item))}'
                )
            if status == 'changed':
                statement = (
                    f'updated. From '
                    f'{dump_values(ig.get_init_value(item))} '
                    f'to {dump_values(ig.get_new_value(item))}'
                )
            return (dump_values(path), statement)
        elif status == 'modified':
            return(
                list(map(
                    lambda node: recourse(node, path),
                    ig.get_children(item)
                ))
            )
    return flatten(list(map(lambda x: recourse(x, path=''), inp_diff)))


def dump_values(value):
    if not isinstance(value, dict):
        if isinstance(value, str):
            return f"'{dump(value)}'"
        return dump(value)
    else:
        return '[complex value]'


def flatten(inp_list):
    a = []

    def recourse(item):
        if not isinstance(item, list):
            a.append(item)
        else:
            list(map(recourse, item))
    recourse(inp_list)
    return a
