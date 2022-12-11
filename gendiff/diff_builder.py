def dict_diff(files):
    '''Return difference list'''
    file1, file2 = files
    sorted_keys = sorted(list(set(
        list(file1.keys()) + list(file2.keys())
    )))

    def key_diff(key):
        diff_node = {}
        diff_node['name'] = key
        if key in file1 and key not in file2:
            diff_node['node_type'] = 'deleted'
            diff_node['values'] = file1[key]
        if key not in file1 and key in file2:
            diff_node['node_type'] = 'added'
            diff_node['values'] = file2[key]
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff_node['node_type'] = 'saved'
                diff_node['values'] = file2[key]
            else:
                file_types = map(
                    lambda x: isinstance(x, dict),
                    (file1[key], file2[key])
                )
                if not all(file_types):
                    diff_node['node_type'] = 'changed'
                    diff_node['values'] = [file1[key], file2[key]]
                else:
                    diff_node['node_type'] = 'modified'
                    diff_node['children'] = dict_diff((file1[key], file2[key]))
        return diff_node
    return list(map(key_diff, sorted_keys))
