import pandas as pd
import sys

filepath = sys.argv[1]
newfile = sys.argv[2]

df = pd.read_csv(filepath)

valid_trials = df.loc[df['valid'] == True]

valid_trials.to_csv(newfile, index = False)