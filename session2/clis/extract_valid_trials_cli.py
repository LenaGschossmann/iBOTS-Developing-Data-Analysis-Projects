import pandas as pd
import argparse as ap

# Create parser and arguments
parser = ap.ArgumentParser(description="Extract valid trials.")
parser.add_argument('inpath', type=str, help='path of input file.')
parser.add_argument('outpath', type=str, help='path of output file.')
args = parser.parse_args()

# Load the csv file and extract active trials
df = pd.read_csv(args.inpath)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(args.outpath, index=False)