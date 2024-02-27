import matplotlib.pyplot as plt
import seaborn as sns


def create_plot(data, xlabel, ylabel, color="k", alpha=1, figsz=(4, 3), dpi=150):
    fig, ax = plt.subplots(figsize=figsz, dpi=dpi)
    ax.plot(data, c=color, alpha=alpha)
    # ax.set_xlabel(xlabel)
    # ax.set_ylabel(ylabel)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    # sns.despine(trim=True)


