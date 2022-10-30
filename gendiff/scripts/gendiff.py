import argparse
from gendiff.scripts import diff_builder
from gendiff.scripts import diff_out


def generate_diff(first_file_path, second_file_path, style):
    return diff_out._out(
        diff_builder.make_diff(
            first_file_path,
            second_file_path,
        ),
        style,
    )


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file_path')
    parser.add_argument('second_file_path')
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='stylish',
        help='set format of output')
    args = parser.parse_args()
    style = args.format
    print(generate_diff(args.first_file_path, args.second_file_path, style))


if __name__ == '__main__':
    main()
