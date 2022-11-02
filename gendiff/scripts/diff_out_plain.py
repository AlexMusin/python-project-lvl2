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
                statement = (f'added with value: '
                f'{dump_values(ig.get_all_values(item))}')
            if status == 'changed':
                statement = (f'updated. From '
                f'{dump_values(ig.get_init_value(item))} '
                f'to {dump_values(ig.get_new_value(item))}')
            return (dump_values(path), statement)
        elif status == 'modified':
            return(list(map(lambda node: recourse(node, path), ig.get_children(item))))
    return flatten(list(map(lambda x: recourse(x, path=''), inp_diff)))


def dump_values(value):
    if not isinstance(value, dict):
        if isinstance(value, str):
            return f"'{dump(value)}'"
        return dump(value)
    else:
        return '[complex value]'


def flatten(inp_list):
    a=[]
    def recourse(item):
        if not isinstance(item, list):
            a.append(item)
        else:
            list(map(recourse, item))
    recourse(inp_list)
    return a


#data = [{'name': 'follow', 'status': 'deleted', 'values': False}, {'name': 'host', 'status': 'saved', 'values': 'hexlet.io'}, {'name': 'nest', 'status': 'modified', 'children': [{'name': 'name', 'status': 'changed', 'values': ['Any', 'Smb']}]}, {'name': 'proxy', 'status': 'deleted', 'values': '123.234.53.22'}, {'name': 'timeout', 'status': 'changed', 'values': [50, 20]}, {'name': 'verbose', 'status': 'added', 'values': True}]
#data2 = [{'name': 'common', 'status': 'modified', 'children': [{'name': 'follow', 'status': 'added', 'values': False}, {'name': 'setting1', 'status': 'saved', 'values': 'Value 1'}, {'name': 'setting2', 'status': 'deleted', 'values': 200}, {'name': 'setting3', 'status': 'changed', 'values': [True, None]}, {'name': 'setting4', 'status': 'added', 'values': 'blah blah'}, {'name': 'setting5', 'status': 'added', 'values': {'key5': 'value5'}}, {'name': 'setting6', 'status': 'modified', 'children': [{'name': 'doge', 'status': 'modified', 'children': [{'name': 'wow', 'status': 'changed', 'values': ['', 'so much']}]}, {'name': 'key', 'status': 'saved', 'values': 'value'}, {'name': 'ops', 'status': 'added', 'values': 'vops'}]}]}, {'name': 'group1', 'status': 'modified', 'children': [{'name': 'baz', 'status': 'changed', 'values': ['bas', 'bars']}, {'name': 'foo', 'status': 'saved', 'values': 'bar'}, {'name': 'nest', 'status': 'changed', 'values': [{'key': 'value'}, 'str']}]}, {'name': 'group2', 'status': 'deleted', 'values': {'abc': 12345, 'deep': {'id': 45}}}, {'name': 'group3', 'status': 'added', 'values': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

#print(out_plain(data2))

#print(flatten([1, [2], [3, [4]]]))

#print(dump_values(10))