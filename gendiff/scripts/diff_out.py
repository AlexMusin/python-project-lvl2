import diff_inner_representation as ig
from dumper import dump

def out_(inp_diff, style='stylish', extention='.json'):
    if style == 'stylish':
        replacer = '    '
    a = ['{']
    def recourse(elem, i=1):
        for item in elem:
            single_status_list = ['saved', 'deleted', 'added']
            if ig.get_status(item) in single_status_list:
                builded_value = single_value_build(
                    ig.get_all_values(item),
                    i,
                    replacer,
                    extention,
                )
            if ig.get_status(item) == 'changed':
                builded_init_value = single_value_build(
                    ig.get_init_value(item),
                    i,
                    replacer,
                    extention,
                )
                builded_new_value = single_value_build(
                    ig.get_new_value(item),
                    i,
                    replacer,
                    extention,
                )
            if ig.get_status(item) == 'saved':
                a.append(f"{replacer * i}    {ig.get_name(item)}: {builded_value}")
            if ig.get_status(item) == 'deleted':
                a.append(f"{replacer * i}  - {ig.get_name(item)}: {builded_value}")
            elif ig.get_status(item) == 'added':
                a.append(f"{replacer * i}  + {ig.get_name(item)}: {builded_value}")
            elif ig.get_status(item) == 'changed':
                a.append(f"{replacer * i}  - {ig.get_name(item)}: {builded_init_value}")
                a.append(f"{replacer * i}  + {ig.get_name(item)}: {builded_new_value}")
            elif ig.get_status(item) == 'modified':
                a.append(f"{replacer * i}    {ig.get_name(item)}: {{")
                i += 1
                recourse(ig.get_children(item), i)
                a.append(f"{replacer * i}}}")
                i -=1
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
                    out_list.append(f"{replacer * depth}    {item}: {dump(elem[item], extention)}")
                else:
                    out_list.append(f"{replacer * depth}    {item}: {{")
                    depth += 1
                    recourse(elem[item], depth)
                    out_list.append(f"{replacer * depth}}}")
                    depth -= 1
        recourse(inp_value, depth)
        out_list.append(f"{replacer * depth}}}")  
    return ('\n'.join(out_list))





data = [{'name': 'follow', 'status': 'deleted', 'values': False}, 
{'name': 'host', 'status': 'saved', 'values': 'hexlet.io'}, 
{'name': 'nest', 'status': 'modified', 'children': 
[{'name': 'name', 'status': 'changed', 'values': 
['Any', 'Smb']}]}, {'name': 'proxy', 'status': 'deleted', 'values': '123.234.53.22'}, 
{'name': 'timeout', 'status': 'changed', 'values': [50, 20]}, 
{'name': 'verbose', 'status': 'added', 'values': True}]

data2 = [{'name': 'common', 'status': 'modified',
'children': [{'name': 'follow', 'status': 'added', 'values': False}, 
{'name': 'setting1', 'status': 'saved', 'values': 'Value 1'}, 
{'name': 'setting2', 'status': 'deleted', 'values': 200}, 
{'name': 'setting3', 'status': 'changed', 'values': [True, None]}, 
{'name': 'setting4', 'status': 'added', 'values': 'blah blah'}, 
{'name': 'setting5', 'status': 'added', 'values': {'key5': 'value5'}}, 
{'name': 'setting6', 'status': 'modified', 
'children': [{'name': 'doge', 'status': 'modified', 
'children': [{'name': 'wow', 'status': 'changed', 'values': ['', 'so much']}]}, 
{'name': 'key', 'status': 'saved', 'values': 'value'}, 
{'name': 'ops', 'status': 'added', 'values': 'vops'}]}]}, 
{'name': 'group1', 'status': 'modified', 'children': 
[{'name': 'baz', 'status': 'changed', 'values': ['bas', 'bars']}, 
{'name': 'foo', 'status': 'saved', 'values': 'bar'}, 
{'name': 'nest', 'status': 'changed', 'values': [{'key': 'value'}, 'str']}]}, 
{'name': 'group2', 'status': 'deleted', 'values': {'abc': 12345, 'deep': {'id': 45}}}, 
{'name': 'group3', 'status': 'added', 'values': {'deep': {'id': {'number': 45}}, 
'fee': 100500}}]

inp_dict = {'deep': {'id': {'number': 45}}, 'fee': 100500}

print(out_(data2))
#saved_dict_build(inp_dict, 1, '    ')
