import gendiff.diff_inner_representation as ig
from gendiff.dumper import dump
from gendiff import node_type as nt


SINGLE_NODE_TYPE_DICT = {
    'saved': ' ',
    'deleted': '-',
    'added': '+'
}
REPLACER = '    '


def out(inp_diff, extention='.json'):
    '''Return stylish-formatted difference'''
    a = ['{']
    node_types = nt.type()

    def recourse(elem, depth=0):
        sorted_elem = sorted(elem, key=lambda k: k['name'])
        for item in sorted_elem:
            name = ig.get_name(item)
            node_type = ig.get_node_type(item)
            if node_type in SINGLE_NODE_TYPE_DICT.keys():
                operation = SINGLE_NODE_TYPE_DICT[node_type]
                builded_value = single_value_build(
                    ig.get_all_values(item),
                    depth,
                    REPLACER,
                    extention,
                )
                a.append(make_string(
                    REPLACER,
                    depth,
                    name,
                    operation,
                    builded_value,
                )
                )
            elif node_type == node_types['changed']:
                operation1 = SINGLE_NODE_TYPE_DICT['deleted']
                operation2 = SINGLE_NODE_TYPE_DICT['added']
                builded_init_value = single_value_build(
                    ig.get_init_value(item),
                    depth,
                    REPLACER,
                    extention,
                )
                builded_new_value = single_value_build(
                    ig.get_new_value(item),
                    depth,
                    REPLACER,
                    extention,
                )
                a.append(make_string(
                    REPLACER,
                    depth,
                    name,
                    operation1,
                    builded_init_value,
                )
                )
                a.append(make_string(
                    REPLACER,
                    depth,
                    name,
                    operation2,
                    builded_new_value,
                )
                )
            elif node_type == node_types['nested']:
                a.append(f"{REPLACER * depth}    {name}: {{")
                depth += 1
                recourse(ig.get_children(item), depth)
                a.append(f"{REPLACER * depth}}}")
                depth -= 1
    recourse(inp_diff)
    a.append('}')
    out_string = '\n'.join(a)
    return out_string


def single_value_build(inp_value, depth, REPLACER, extention):
    '''Build output for single complex cases
    i.e. when node_type is not nested and
    at least one of the values is complex'''
    out_list = []
    depth += 1
    if not isinstance(inp_value, dict):
        out_list.append(f'{dump(inp_value, extention)}')
    else:
        out_list.append('{')

        def recourse(elem, depth):
            for item in sorted(elem.keys()):
                if not isinstance(elem[item], dict):
                    out_list.append(
                        f"{REPLACER * depth}    "
                        f"{item}: {dump(elem[item], extention)}"
                    )
                else:
                    out_list.append(f"{REPLACER * depth}    {item}: {{")
                    depth += 1
                    recourse(elem[item], depth)
                    out_list.append(f"{REPLACER * depth}}}")
                    depth -= 1
        recourse(inp_value, depth)
        out_list.append(f"{REPLACER * depth}}}")
    return ('\n'.join(out_list))


def make_string(REPLACER, depth, name, operation, value):
    return (
        f"{REPLACER * depth}  {operation} "
        f"{name}: "
        f"{value}"
    )
