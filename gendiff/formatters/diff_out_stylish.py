import gendiff.diff_inner_representation as ig
from gendiff.dumper import dump


SIMPLE_NODE_TYPE_DICT = {
    'saved': ' ',
    'deleted': '-',
    'added': '+'
}
INDENT = '    '
NESTED = 'nested'
SAVED = 'saved'
DELETED = 'deleted'
ADDED = 'added'
CHANGED = 'changed'
NAME = 'name'


def out(inp_diff):
    '''Return stylish-formatted difference'''
    result_list = ['{']

    def recourse(elem, depth=0):
        sorted_elem = sorted(elem, key=lambda k: k[NAME])
        for item in sorted_elem:
            name = ig.get_name(item)
            node_type = ig.get_node_type(item)
            if node_type in SIMPLE_NODE_TYPE_DICT.keys():
                operation = SIMPLE_NODE_TYPE_DICT[node_type]
                formatted_node = make_formatted_node(
                    ig.get_all_values(item),
                    depth,
                    INDENT,
                    name,
                    operation
                )
                result_list.append(formatted_node)
            elif node_type == CHANGED:
                operation1 = SIMPLE_NODE_TYPE_DICT[DELETED]
                operation2 = SIMPLE_NODE_TYPE_DICT[ADDED]
                init_node = make_formatted_node(
                    ig.get_init_value(item),
                    depth,
                    INDENT,
                    name,
                    operation1
                )
                new_node = make_formatted_node(
                    ig.get_new_value(item),
                    depth,
                    INDENT,
                    name,
                    operation2
                )
                formatted_node = init_node + '\n' + new_node
                result_list.append(formatted_node)
            elif node_type == NESTED:
                depth += 1
                result_list.append(f"{INDENT * depth}{name}: {{")
                recourse(ig.get_children(item), depth)
                result_list.append(f"{INDENT * depth}}}")
                depth -= 1
    recourse(inp_diff)
    result_list.append('}')
    out_string = '\n'.join(result_list)
    return out_string


def build_value_string(depth, INDENT, inp_value):
    '''Build output for single value'''
    out_list = []
    depth += 1
    if not isinstance(inp_value, dict):
        out_list.append(f'{dump(inp_value)}')
    else:
        out_list.append('{')

        def recourse(elem, depth):
            for item in sorted(elem.keys()):
                if not isinstance(elem[item], dict):
                    out_list.append(
                        f"{INDENT * depth}    "
                        f"{item}: {dump(elem[item])}"
                    )
                else:
                    out_list.append(f"{INDENT * depth}    {item}: {{")
                    depth += 1
                    recourse(elem[item], depth)
                    out_list.append(f"{INDENT * depth}}}")
                    depth -= 1
        recourse(inp_value, depth)
        out_list.append(f"{INDENT * depth}}}")
    return ('\n'.join(out_list))


def make_long_string(depth, INDENT, name, operation, value_string):
    return (
        f"{INDENT * depth}  {operation} "
        f"{name}: "
        f"{value_string}"
    )


def make_formatted_node(inp_value, depth, INDENT, name, operation):
    value_string = build_value_string(
        depth,
        INDENT,
        inp_value,
    )
    formatted_node = make_long_string(
        depth,
        INDENT,
        name,
        operation,
        value_string
    )
    return formatted_node
