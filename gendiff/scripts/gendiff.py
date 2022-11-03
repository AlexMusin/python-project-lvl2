import argparse
from gendiff.scripts import diff_builder
from gendiff.scripts import diff_out_plain
from gendiff.scripts import diff_out_stylish


def generate_diff(first_file_path, second_file_path, format):
    if format == 'stylish':
        return diff_out_stylish.out_stylish(
            diff_builder.make_diff(
                first_file_path,
                second_file_path,
            )
        )
    if format == 'plain':
        return diff_out_plain.out_plain(
            diff_builder.make_diff(
                first_file_path,
                second_file_path,
            )
        )


def main():
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
    print(generate_diff(args.first_file_path, args.second_file_path, format))


if __name__ == '__main__':
    main()
