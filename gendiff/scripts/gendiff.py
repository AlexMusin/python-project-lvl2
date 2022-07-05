import argparse


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument(metavar='first_file', dest = 'accumulate')
parser.add_argument(metavar='second_file', dest = 'accumulate')
args = parser.parse_args()
print(args.accumulate(args.integers))



def main():
    print('aaa')


if __name__ == '__main__':
    main()