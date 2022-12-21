NESTED = 'nested'
SAVED = 'saved'
DELETED = 'deleted'
ADDED = 'added'
CHANGED = 'changed'
NODE_TYPE = 'node_type'
VALUES = 'values'
NAME = 'name'
CHILDREN = 'children'


def dict_diff(dict1, dict2):
    '''Return difference list'''
    keys_set = set(
        list(dict1.keys()) + list(dict2.keys())
    )

    def key_diff(key):
        diff_node = {}
        diff_node[NAME] = key
        collection_is_dict = map(
            lambda x: isinstance(x, dict),
            (dict1.get(key), dict2.get(key))
        )
        if key in dict1 and key not in dict2:
            diff_node[NODE_TYPE] = DELETED
            diff_node[VALUES] = dict1[key]
        elif key not in dict1 and key in dict2:
            diff_node[NODE_TYPE] = ADDED
            diff_node[VALUES] = dict2[key]
        elif dict1[key] == dict2[key]:
            diff_node[NODE_TYPE] = SAVED
            diff_node[VALUES] = dict2[key]
        elif all(collection_is_dict):
            diff_node[NODE_TYPE] = NESTED
            diff_node[CHILDREN] = dict_diff(dict1[key], dict2[key])
        else:
            diff_node[NODE_TYPE] = CHANGED
            diff_node[VALUES] = [dict1[key], dict2[key]]
        return diff_node
    return list(map(key_diff, keys_set))
