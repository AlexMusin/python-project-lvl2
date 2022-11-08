import argparse
from gendiff.diff_launcher import generate_diff


def main():
    '''Launch diff launcher with input arguments'''
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
    print(generate_diff(args.first_file_path, args.second_file_path, args.format))


if __name__ == '__main__':
    main()
