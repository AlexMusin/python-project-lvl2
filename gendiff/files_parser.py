from gendiff import parser


def parse_files(files):
    file1_tup, file2_tup = files
    parsed_file1 = parser.parse_file(file1_tup)
    parsed_file2 = parser.parse_file(file2_tup)
    return (parsed_file1, parsed_file2)
