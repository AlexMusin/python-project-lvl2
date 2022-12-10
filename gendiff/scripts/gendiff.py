import argparse
from gendiff.diff_generator import generate_diff


FORMAT_TUP = (
    'stylish',
    'plain',
    'json',
)


def cli():
    '''Launch difference building and return it with defined formater'''
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
    if format not in FORMAT_TUP:
        print('''User defined format is not available.
        Format switched to "stylish"''')
        format = 'stylish'
    print(generate_diff(first_file_path, second_file_path, format))


def main():
    cli()


if __name__ == '__main__':
    main()
