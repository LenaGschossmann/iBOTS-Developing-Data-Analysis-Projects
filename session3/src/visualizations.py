import matplotlib.pyplot as plt

def plot_histogram(data, nbins=50, color='black'):
    figure, ax = plt.subplots(ncols=1, nrows=1)
    ax.hist(data, bins=nbins, color=color)