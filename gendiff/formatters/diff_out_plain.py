import gendiff.diff_inner_representation as ig
from gendiff.dumper import dump


NESTED = 'nested'
SAVED = 'saved'
DELETED = 'deleted'
ADDED = 'added'
CHANGED = 'changed'
NAME = 'name'


def out(inp_diff):
    result_list = []

    def recourse(elem, path):
        sorted_elem_list = sorted(elem, key=lambda k: k[NAME])
        for item in sorted_elem_list:
            name = ig.get_name(item)
            node_type = ig.get_node_type(item)
            path_old = path
            path = ('.'.join([path, name])).strip('.')
            if node_type == NESTED:
                recourse(ig.get_children(item), path)
            elif node_type != SAVED:
                if node_type == DELETED:
                    statement = 'removed'
                elif node_type == ADDED:
                    statement = (
                        f'added with value: '
                        f'{dump_values(ig.get_all_values(item))}'
                    )
                elif node_type == CHANGED:
                    statement = (
                        f'updated. From '
                        f'{dump_values(ig.get_init_value(item))} '
                        f'to {dump_values(ig.get_new_value(item))}'
                    )
                formatted_node = make_formatted_node(path, statement)
                result_list.append(formatted_node)
            path = path_old
    recourse(inp_diff, path='')
    out_string = '\n'.join(result_list)
    return out_string


def make_formatted_node(path, statement):
    return f"Property '{path}' was {statement}"


def dump_values(value):
    '''JSON-format value dumper'''
    if not isinstance(value, dict):
        if isinstance(value, str):
            return f"'{dump(value)}'"
        return dump(value)
    else:
        return '[complex value]'
