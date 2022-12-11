from os import path


FORMAT_LIST = ['.json', '.yaml', '.yml']


def read_file(file_path):
    '''
    Read file from input paths
    Check format by extention
    Return text and format in tuple
    '''
    extention = path.splitext(file_path)[1]
    if extention not in FORMAT_LIST:
        raise Exception('Wrong file format!')
    with open(file_path, 'r') as f:
        text = f.read()
        return (text, extention)
