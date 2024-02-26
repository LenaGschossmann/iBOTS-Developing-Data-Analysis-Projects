import argparse as ap

parser = ap.ArgumentParser(description="Sqaure a number.")

parser.add_argument('number', type=int, help='any integer')

args = parser.parse_args()

print(f'The square of {args.number} is {args.number**2}.')