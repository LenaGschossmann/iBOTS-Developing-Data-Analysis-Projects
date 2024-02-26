import argparse as ap
import pandas as pd
import os
import glob
from tqdm import tqdm
import json, pathlib

# Create parser
parser = ap.ArgumentParser(description= "Merge task data.")
parser.add_argument('sessiondir', type=str, help='path to session directory')
parser.add_argument('outdir', type=str, help="directory for saving final csv file")
args = parser.parse_args()

# Obtain metadata
metadata_path = glob.glob(args.sessiondir + '*.json')[0]
metadata = pathlib.Path(metadata_path).read_text()
parsed_metadata = json.loads(metadata)

# Obtain files in input folder
task_data_path = os.path.join(args.sessiondir, 'task', '') 
task_filelist = glob.glob(task_data_path + '*.csv')

perf_data_path = os.path.join(args.sessiondir, 'performance', '') 
perf_filelist = glob.glob(perf_data_path + '*.csv')

# Loop through task files:
dfs = []
for idx,file in tqdm(enumerate(task_filelist)):
    dfs.append(pd.read_csv(file))
task_df = pd.concat(dfs)
task_df.set_index('trial')

dfs = []
for idx,file in tqdm(enumerate(perf_filelist)):
    dfs.append(pd.read_csv(file))
perf_df = pd.concat(dfs)
perf_df.set_index('trial')

# Final DataFrame
outdf = pd.merge(task_df, perf_df, how='outer')

outdf['session_date'] = parsed_metadata['session_date']
outdf['mouse'] = parsed_metadata['mouse']
outdf['stim_onset'] = parsed_metadata['stim_onset']
outdf['bin_size'] = parsed_metadata['bin_size']

# Define output path
out_path = os.path.join(args.outdir, parsed_metadata['mouse'] + '_' + parsed_metadata['session_date'] + '.csv')

# Write csv
outdf.to_csv(out_path, index=False)


