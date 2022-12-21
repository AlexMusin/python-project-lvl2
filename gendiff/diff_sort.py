from gendiff import diff_inner_representation as ig


def sort_diff(diff):
    diff.sort(key=lambda k: ig.get_name(k))
    for elem in diff:
        if ig.get_node_type(elem) == 'nested':
            sort_diff(ig.get_children(elem))
    return diff
