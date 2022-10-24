import parser as file_parser
import copy
from os import path

def build_diff(first_file_path, second_file_path):
    file1_extention = path.splitext(first_file_path)[1]
    file2_extention = path.splitext(second_file_path)[1]
    first_file = file_parser.parse(first_file_path, file1_extention)
    second_file = file_parser.parse(second_file_path, file2_extention)
    return make_diff(first_file, second_file)


def make_diff(first_file, second_file):
    #print(first_file)
    #print(second_file)
    sorted_keys = sorted(list(set(list(first_file.keys())
                                  + list(second_file.keys()))))
    diff_node = {}
    for key in sorted_keys:
        diff_node['name'] = str(key)
        diff_node['children'] = []
        elem1 = first_file.get(key, 'no_value')
        elem2 = first_file.get(key, 'no_value')
        if elem1 != elem2:
            if elem1 == 'no_value':
                children = []
            diff_node['status'] = 'changed'
            diff_node['children'].append(elem1, elem2)
   

            #print(merged_dict[element])
    #make_diff() 
            #if type(element) ==

def do_diff(file1_path, file2_path):    
    file1_extention = path.splitext(file1_path)[1]
    file2_extention = path.splitext(file2_path)[1]
    file1 = file_parser.parse(file1_path, file1_extention)
    file2 = file_parser.parse(file2_path, file2_extention)
    
    def r1(file1, file2):

        sorted_keys = sorted(list(set(list(file1.keys())
                                    + list(file2.keys()))))
        #print(sorted_keys)
        def r2(key):
            diff_node = {}
            #for key in sorted_keys:
            #diff_node = {}
            diff_node['name'] = key
            #diff_node['values'] = []
            if key in file1 and key not in file2:
                diff_node['status'] = 'deleted'
                diff_node['values'] = file1[key]
            if key not in file1 and key in file2:
                diff_node['status'] = 'added'
                diff_node['values'] = file2[key]
            if key in file1 and key in file2:
                if file1[key] == file2[key]:
                    diff_node['status'] = 'saved'
                    diff_node['values'] = file2[key]
                else:
                    if type(file1[key]) != type(file2[key]):
                        diff_node['status'] = 'changed'
                        diff_node['values'] = [file1[key], file2[key]]
                    elif not isinstance(file1[key], dict):
                        diff_node['status'] = 'changed'
                        diff_node['values'] = [file1[key], file2[key]]
                    else:
                        diff_node['status'] = 'modified'
                        #children = diff_recourse(file1[key], file2[key])
                        #print(children)
                        #print(r1(file1[key], file2[key]))
                        diff_node['values'] = r1(file1[key], file2[key])
            #print(diff_node)
            return diff_node

        return list(map(r2, sorted_keys))
    return r1(file1, file2)
    #return recourse(file1, file2)

    #return do_diff(file1, file2)
    #return diff







        



print(do_diff('../../tests/fixtures/file1.json', '../../tests/fixtures/file2.json'))