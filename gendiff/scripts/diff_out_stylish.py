import gendiff.scripts.diff_inner_representation as ig
from gendiff.scripts.dumper import dump


SINGLE_STATUS_DICT = {
    'saved': ' ',
    'deleted': '-',
    'added': '+'
}


def out_stylish(inp_diff, extention='.json'):
    '''Return stylish-formatted difference'''
    replacer = '    '
    a = ['{']

    def recourse(elem, depth=0):
        for item in elem:
            name = ig.get_name(item)
            status = ig.get_status(item)
            if status in SINGLE_STATUS_DICT.keys():
                operation = SINGLE_STATUS_DICT[status]
                builded_value = single_value_build(
                    ig.get_all_values(item),
                    depth,
                    replacer,
                    extention,
                )
                a.append(make_string(
                    replacer,
                    depth,
                    name,
                    operation,
                    builded_value,
                )
                )
            elif status == 'changed':
                operation1 = SINGLE_STATUS_DICT['deleted']
                operation2 = SINGLE_STATUS_DICT['added']
                builded_init_value = single_value_build(
                    ig.get_init_value(item),
                    depth,
                    replacer,
                    extention,
                )
                builded_new_value = single_value_build(
                    ig.get_new_value(item),
                    depth,
                    replacer,
                    extention,
                )
                a.append(make_string(
                    replacer,
                    depth,
                    name,
                    operation1,
                    builded_init_value,
                )
                )
                a.append(make_string(
                    replacer,
                    depth,
                    name,
                    operation2,
                    builded_new_value,
                )
                )
            elif status == 'modified':
                a.append(f"{replacer * depth}    {name}: {{")
                depth += 1
                recourse(ig.get_children(item), depth)
                a.append(f"{replacer * depth}}}")
                depth -= 1
    recourse(inp_diff)
    a.append('}')
    out_string = '\n'.join(a)
    return out_string


def single_value_build(inp_value, depth, replacer, extention):
    '''Build output for single complex cases
    i.e. when status is not modified and
    at least one of the values is complex'''
    out_list = []
    depth += 1
    if not isinstance(inp_value, dict):
        out_list.append(f'{dump(inp_value, extention)}')
    else:
        out_list.append('{')

        def recourse(elem, depth):
            for item in elem:
                if not isinstance(elem[item], dict):
                    out_list.append(
                        f"{replacer * depth}    "
                        f"{item}: {dump(elem[item], extention)}"
                    )
                else:
                    out_list.append(f"{replacer * depth}    {item}: {{")
                    depth += 1
                    recourse(elem[item], depth)
                    out_list.append(f"{replacer * depth}}}")
                    depth -= 1
        recourse(inp_value, depth)
        out_list.append(f"{replacer * depth}}}")
    return ('\n'.join(out_list))


def make_string(replacer, depth, name, operation, value):
    return (
        f"{replacer * depth}  {operation} "
        f"{name}: "
        f"{value}"
    )
