import argparse
import json
from os import path
from gendiff.scripts import dumper
from gendiff.scripts import parser as file_parser


def generate_diff(first_file_path, second_file_path):
    file1_extention = path.splitext(first_file_path)[1]
    file2_extention = path.splitext(second_file_path)[1]
    first_file = file_parser.parse(first_file_path, file1_extention)
    second_file = file_parser.parse(second_file_path, file2_extention)
    sorted_keys = sorted(list(set(list(first_file.keys())
                                  + list(second_file.keys()))))
    out_string = '{'
    for key in sorted_keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                out_string += (
                    '\n    '
                    + dumper.dump(key, file1_extention)
                    + ': '
                    + dumper.dump(first_file[key], file1_extention)
                )
            else:
                out_string += (
                    '\n  - '
                    + dumper.dump(key, file1_extention)
                    + ': '
                    + dumper.dump(first_file[key], file1_extention)
                )
                out_string += (
                    '\n  + '
                    + dumper.dump(key, file1_extention)
                    + ': '
                    + dumper.dump(second_file[key], file2_extention)
                )
        elif key not in second_file:
            out_string += (
                '\n  - '
                + dumper.dump(key, file1_extention)
                + ': '
                + dumper.dump(first_file[key], file1_extention)
            )
        elif key not in first_file:
            out_string += (
                '\n  + '
                + dumper.dump(key, file1_extention)
                + ': '
                + dumper.dump(second_file[key], file2_extention)
            )
    out_string += '\n}'
    return out_string


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file_path')
    parser.add_argument('second_file_path')
    parser.add_argument(
        '-f', '--format',
        dest='format',
        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file_path, args.second_file_path))


if __name__ == '__main__':
    main()
