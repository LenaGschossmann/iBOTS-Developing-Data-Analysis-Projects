import glob
import numpy as np
from tqdm import tqdm
from scipy.io import loadmat
import re

def load_data(input_dir, file_exp, description='None'):
    all_files = glob.glob(input_dir + file_exp)

    if (re.search('npy',file_exp)) != None:
        load_func = np.load
    elif re.search('mat',file_exp) is not None:
        load_func = loadmat
        
    data = []
    for filename in tqdm(all_files, desc=description):
        data_per_trial = load_func(filename)
        data.append(data_per_trial)

    data = np.stack(data)
    return data