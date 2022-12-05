import argparse
from gendiff import diff_builder
from gendiff.files_input import read_files
from gendiff.files_parser import parse_files
from gendiff.diff_out import diff_output


FORMAT_LIST = [
    'stylish',
    'plain',
    'json',
]


def generate_diff(first_file_path, second_file_path, format):
    files = read_files(first_file_path, second_file_path)
    parsed_files = parse_files(files)
    difference = diff_builder.dict_diff(parsed_files)
    diff_out = diff_output(difference, format)
    return diff_out


def cli():
    '''Launch difference building and output it with defined formater'''
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
    first_file_path = args.first_file_path
    second_file_path = args.second_file_path
    if format not in FORMAT_LIST:
        print('''User defined format is not available.
        Format switched to "stylish"''')
        format = 'stylish'
    generate_diff(first_file_path, second_file_path, format)


def main():
    cli()


if __name__ == '__main__':
    main()
