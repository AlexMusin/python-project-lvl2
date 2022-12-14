from gendiff import node_type


def dict_diff(dict1, dict2):
    '''Return difference list'''
    node_types = node_type.type()
    sorted_keys = sorted(list(set(
        list(dict1.keys()) + list(dict2.keys())
    )))

    def key_diff(key):
        diff_node = {}
        diff_node['name'] = key
        if key in dict1 and key not in dict2:
            diff_node['node_type'] = node_types['deleted']
            diff_node['values'] = dict1[key]
        if key not in dict1 and key in dict2:
            diff_node['node_type'] = node_types['added']
            diff_node['values'] = dict2[key]
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                diff_node['node_type'] = node_types['saved']
                diff_node['values'] = dict2[key]
            else:
                collection_types = map(
                    lambda x: isinstance(x, dict),
                    (dict1[key], dict2[key])
                )
                if not all(collection_types):
                    diff_node['node_type'] = node_types['changed']
                    diff_node['values'] = [dict1[key], dict2[key]]
                else:
                    diff_node['node_type'] = node_types['nested']
                    diff_node['children'] = dict_diff(dict1[key], dict2[key])
        return diff_node
    return list(map(key_diff, sorted_keys))
