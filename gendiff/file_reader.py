from os import path


def read_file(file_path):
    '''
    Read file from input paths
    Return text and format in tuple
    '''
    extention = path.splitext(file_path)[1]
    with open(file_path, 'r') as f:
        text = f.read()
        return (text, extention)
