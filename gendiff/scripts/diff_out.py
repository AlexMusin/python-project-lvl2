import gendiff.scripts.diff_inner_representation as ig
from gendiff.scripts.dumper import dump


def _out(inp_diff, style='stylish', extention='.json'):
    if style == 'stylish':
        replacer = '    '
    a = ['{']

    def recourse(elem, depth=0):
        for item in elem:
            single_status_list = ['saved', 'deleted', 'added']
            if ig.get_status(item) in single_status_list:
                builded_value = single_value_build(
                    ig.get_all_values(item),
                    depth,
                    replacer,
                    extention,
                )
            if ig.get_status(item) == 'changed':
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
            if ig.get_status(item) == 'saved':
                a.append(
                    f"{replacer * depth}    "
                    f"{ig.get_name(item)}: "
                    f"{builded_value}"
                )
            if ig.get_status(item) == 'deleted':
                a.append(
                    f"{replacer * depth}  - "
                    f"{ig.get_name(item)}: "
                    f"{builded_value}"
                )
            elif ig.get_status(item) == 'added':
                a.append(
                    f"{replacer * depth}  + "
                    f"{ig.get_name(item)}: "
                    f"{builded_value}"
                )
            elif ig.get_status(item) == 'changed':
                a.append(
                    f"{replacer * depth}  - "
                    f"{ig.get_name(item)}: "
                    f"{builded_init_value}"
                )
                a.append(
                    f"{replacer * depth}  + "
                    f"{ig.get_name(item)}: "
                    f"{builded_new_value}"
                )
            elif ig.get_status(item) == 'modified':
                a.append(f"{replacer * depth}    {ig.get_name(item)}: {{")
                depth += 1
                recourse(ig.get_children(item), depth)
                a.append(f"{replacer * depth}}}")
                depth -= 1
    recourse(inp_diff)
    a.append('}')
    out_string = '\n'.join(a)
    return out_string


def single_value_build(inp_value, depth, replacer, extention):
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
