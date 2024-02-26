import argparse as ap
import pandas as pd
import os
import glob
from tqdm import tqdm
import json, pathlib

# Create parser
parser = ap.ArgumentParser(description= "Merge task data.")
parser.add_argument('sessiondir', type=str, help='path to session directory')
parser.add_argument('subdir', type=str, help='path to subdirectory with files')
parser.add_argument('outdir', type=str, help="directory for saving final csv file")
args = parser.parse_args()

# Obtain metadata
metadata_path = glob.glob(args.sessiondir + '*.json')[0]
metadata = pathlib.Path(metadata_path).read_text()
parsed_metadata = json.loads(metadata)

# Obtain files in input folder
data_path = os.path.join(args.sessiondir, args.subdir,'') 
filelist = glob.glob(data_path + '*.csv')
nfiles = len(filelist)

# Loop through files:
dfs = []
for idx,file in tqdm(enumerate(filelist)):
    dfs.append(pd.read_csv(file))

# Final DataFrame
outdf = pd.concat(dfs)

outdf['session_date'] = parsed_metadata['session_date']
outdf['mouse'] = parsed_metadata['mouse']
outdf['stim_onset'] = parsed_metadata['stim_onset']
outdf['bin_size'] = parsed_metadata['bin_size']

# Define output path
out_path = os.path.join(args.outdir, args.subdir + '_' + parsed_metadata['mouse'] + '_' + parsed_metadata['session_date'] + '.csv')

# Write csv
outdf.to_csv(out_path, index=False)


