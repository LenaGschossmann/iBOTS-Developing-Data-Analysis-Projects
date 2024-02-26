import argparse as ap

parser = ap.ArgumentParser(description="Sqaure a number.")

parser.add_argument('number1', type=float, help='any float')
parser.add_argument('number2', type=float, help='any float')
parser.add_argument('--scale', type=float, help='scale sum of numbers.', default=1)

args = parser.parse_args()

print(f'The sum of {args.number1} and {args.number2}, scaled by {args.scale}, is {(args.number1 + args.number2)*args.scale}.')