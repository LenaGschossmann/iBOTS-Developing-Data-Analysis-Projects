import pandas as pd
import argparse as ap
import os

# Create parser and arguments
parser = ap.ArgumentParser(description="Extract valid trials.")
parser.add_argument('inpath', type=str, help='path of input file.')
parser.add_argument('outpath', type=str, help='path of output file.')
parser.add_argument('--subject', type=str, default='all', help='ID of subject whos trials should be extracted.')
args = parser.parse_args()

# Load the csv file
df = pd.read_csv(args.inpath)

# Extract active trials
df_valid = df[df.valid].copy()

# Filter by subject
if args.subject == 'all':
    df_out = df_valid
else:
    subject = int(args.subject)
    df_out = df_valid.loc[df_valid['subject_id'] == subject]

# Define output path
if args.outpath[-3:] == 'npy':
    out_path = args.outpath
else:
    out_path = args.outpath + os.path.split(args.inpath)[1][:-4] + '_valid_' + args.subject + '.csv'

# Save the new dataframe as a csv file
df_out.to_csv(out_path, index=False)