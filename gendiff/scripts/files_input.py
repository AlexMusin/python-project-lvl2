from gendiff import reader

def read_files(file1_path, file2_path):
    '''Read files from input paths'''
    file1 = reader.read_file(file1_path)
    file2 = reader.read_file(file2_path)
    return file1, file2
