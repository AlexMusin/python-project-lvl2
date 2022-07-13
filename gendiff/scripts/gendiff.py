import argparse
import json

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file_path')
parser.add_argument('second_file_path')
parser.add_argument(
    '-f', '--format',
    dest='format',
    help='set format of output')
args = parser.parse_args()


def generate_diff(first_file_path, second_file_path):
    with open(first_file_path, 'r') as f:
        first_file = json.load(f)
    with open(second_file_path, 'r') as f:
        second_file = json.load(f)
    sorted_keys = sorted(list(set(list(first_file.keys())
                                  + list(second_file.keys()))))
    out_string = '{'
    for key in sorted_keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                out_string += (
                    '\n    '
                    + json.dumps(key).strip('"')
                    + ': '
                    + json.dumps(first_file[key]).strip('"')
                )
            else:
                out_string += (
                    '\n  - '
                    + json.dumps(key).strip('"')
                    + ': '
                    + json.dumps(first_file[key]).strip('"')
                )
                out_string += (
                    '\n  + '
                    + json.dumps(key).strip('"')
                    + ': '
                    + json.dumps(second_file[key]).strip('"')
                )
        elif key not in second_file:
            out_string += (
                '\n  - '
                + json.dumps(key).strip('"')
                + ': '
                + json.dumps(first_file[key]).strip('"')
            )
        elif key not in first_file:
            out_string += (
                '\n  + '
                + json.dumps(key).strip('"')
                + ': '
                + json.dumps(second_file[key]).strip('"')
            )
    out_string += '\n}'
    return out_string


def main():
    print(generate_diff(args.first_file_path, args.second_file_path))


if __name__ == '__main__':
    main()
