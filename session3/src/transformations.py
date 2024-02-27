import numpy as np

def normalize(data, lower=0, upper=1):
    min_val = min(data)
    data = np.array(data) - min_val

    max_val = max(data)
    data = (data / max_val)

    data = (data + lower) * (upper-lower)

    # or:
    # [(x-min(data)) / max(data) for x in data]

    return data


def standardize(data):
    return (data - np.mean(data)) / np.std(data)