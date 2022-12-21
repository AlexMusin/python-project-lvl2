from gendiff import node_type


def dict_diff(dict1, dict2):
    '''Return difference list'''
    node_types = node_type.type()
    keys_set = set(
        list(dict1.keys()) + list(dict2.keys())
    )

    def key_diff(key):
        diff_node = {}
        diff_node['name'] = key
        collection_is_dict = map(
            lambda x: isinstance(x, dict),
            (dict1.get(key), dict2.get(key))
        )
        if key in dict1 and key not in dict2:
            diff_node['node_type'] = node_types['deleted']
            diff_node['values'] = dict1[key]
        elif key not in dict1 and key in dict2:
            diff_node['node_type'] = node_types['added']
            diff_node['values'] = dict2[key]
        elif dict1[key] == dict2[key]:
            diff_node['node_type'] = node_types['saved']
            diff_node['values'] = dict2[key]
        elif all(collection_is_dict):
            diff_node['node_type'] = node_types['nested']
            diff_node['children'] = dict_diff(dict1[key], dict2[key])
        else:
            diff_node['node_type'] = node_types['changed']
            diff_node['values'] = [dict1[key], dict2[key]]
        return diff_node
    return list(map(key_diff, keys_set))
