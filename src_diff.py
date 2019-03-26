import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data3/dummy%s.pkl" % j))


def mean_std():
    matrix_means = np.zeros((100, 60))
    matrix_std = np.zeros((100, 60))
    for idx, df in enumerate(data_frames):
        _means = df.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].mean()
        _std = df.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].std()
        team_size = _means['gh_team_size'].tolist()
        row_mean = _means['git_diff_src_churn'].tolist()
        row_std = _std['git_diff_src_churn'].tolist()
        matrix_means[idx][np.array(tuple(team_size))] = row_mean
        matrix_std[idx][np.array(tuple(team_size))] = row_std

    total_mean = np.nanmean(matrix_means, axis=0)
    total_std = np.nanmean(matrix_std, axis=0)
    return total_mean, total_std


def line_plot():
    index = np.arange(means.shape[0])
    fig, ax = plt.subplot()
    ax.plot(index, means, marker='o', color='crimson', linewidth=1)
    ax.set_ylim(bottom=0.)
    plt.xlabel("Team size")
    plt.ylabel("Mean of source code diff")
    plt.legend()
    plt.savefig('figs/src_diff_line.png', dpi=500)
    plt.show()


def scatter_plot():
    index = np.arange(means.shape[0])
    plt.errorbar(index, means, std, linestyle='None', marker='_', lolims=True, elinewidth=0.5, ecolor='crimson',
                 capthick=0.5)
    plt.scatter(index, means, color='crimson', linewidth=0.5)
    plt.xlabel("Team size")
    plt.ylabel("Mean of source code diff")
    plt.legend()
    plt.savefig('figs/src_diff_scatter.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    means, std = mean_std()
    scatter_plot()
    # line_plot()
