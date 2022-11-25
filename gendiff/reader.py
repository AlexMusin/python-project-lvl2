from os import path


EXTENTIONS_LIST = ['.json', '.yaml', '.yml']


def read_file(file_path):
    extention = path.splitext(file_path)[1]
    if extention not in EXTENTIONS_LIST:
        raise Exception('Wrong file extention!')
    with open(file_path, 'r') as f:
        file = f.read()
        return (file, extention)
