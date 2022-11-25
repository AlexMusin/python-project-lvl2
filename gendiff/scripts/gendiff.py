import argparse
from gendiff.scripts import diff_builder
from gendiff.scripts.files_input import read_files
from gendiff.scripts.files_parser import parse_files
from gendiff.scripts.diff_out import diff_output


FORMAT_LIST = [
    'stylish',
    'plain',
    'json',
]


def generate_diff(first_file_path, second_file_path, format):
    'Launch difference building and output it with defined formater'
    files = read_files(first_file_path, second_file_path)
    parsed_files = parse_files(files)
    difference = diff_builder.dict_diff(parsed_files)
    diff_out = diff_output(difference, format)
    return diff_out


def main():
    '''Launch diff launcher with input arguments and prints output'''
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='stylish',
        help='set format of output')
    parser.add_argument('first_file_path')
    parser.add_argument('second_file_path')
    args = parser.parse_args()
    format = args.format
    if format not in FORMAT_LIST:
        print('''User defined format is not available.
        Format switched to "stylish"''')
        format = 'stylish'
    print(generate_diff(
        args.first_file_path,
        args.second_file_path,
        format,
    ))


if __name__ == '__main__':
    main()
