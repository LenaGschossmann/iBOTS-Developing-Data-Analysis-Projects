import numpy as np
import argparse as ap
import os

# Create subparser and arguments
parser = ap.ArgumentParser()

# create subparser object
subparser = parser.add_subparsers(dest='command', required=True)

parser_1 = subparser.add_parser('standardize', help='Standardize the data.')
parser_2 = subparser.add_parser('normalize', help='Normalize the data.')

parser_1.add_argument('inpath', type=str, help='path of input file.')
parser_1.add_argument('outpath', type=str, help='path of output file.')

parser_2.add_argument('inpath', type=str, help='path of input file.')
parser_2.add_argument('outpath', type=str, help='path of output file.')

args = parser.parse_args()

# Load the input
input_array = np.load(args.inpath)

if args.command == 'normalize':
    # normalize it
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)
    out_name_specifier = 'normalized'
elif args.command == 'standardize':
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)
    out_name_specifier = 'standardized'

# Save the normalized array
np.save(args.outpath, output_array)



# # ------------- Not using subparser:
# # Create parser and arguments
# parser = ap.ArgumentParser()
# parser.add_argument('inpath', type=str, help='path of input file.')
# parser.add_argument('outpath', type=str, help='path of output file.')
# parser.add_argument('--transform', type=str, default = 'standardize', choices = ['standardize', 'normalize'], help='type of transformation.')
# args = parser.parse_args()

# # Load the input
# input_array = np.load(args.inpath)

# if args.transform == 'normalize':
#     # normalize it
#     output_array = input_array - np.min(input_array)
#     output_array = output_array / np.max(output_array)
#     out_name_specifier = 'normalized'
# elif args.transform == 'standardize':
#     output_array = (input_array - np.mean(input_array)) / np.std(input_array)
#     out_name_specifier = 'standardized'

# # Define output path
# if args.outpath[-3:] == 'npy':
#     out_path = args.outpath
# else:
#     out_path = args.outpath + os.path.split(args.inpath)[1][:-4] + '_' + out_name_specifier + '.npy'

# # Save the normalized array
# np.save(out_path, output_array)