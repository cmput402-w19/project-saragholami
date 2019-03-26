import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data3/dummy%s.pkl" % j))


def mean_std():
    matrix_means_code = np.zeros((100, 60))
    matrix_std_code = np.zeros((100, 60))
    matrix_means_sloc = np.zeros((100, 60))
    matrix_std_sloc = np.zeros((100, 60))

    for idx, df in enumerate(data_frames):
        _means_code = df.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].mean()
        _std_code = df.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].std()
        _means_sloc = df.groupby('gh_team_size', as_index=False)['gh_sloc'].mean()
        _std_sloc = df.groupby('gh_team_size', as_index=False)['gh_sloc'].std()

        team_size = _means_code['gh_team_size'].tolist()
        row_mean_code = _means_code['git_diff_src_churn'].tolist()
        row_std_code = _std_code['git_diff_src_churn'].tolist()
        row_mean_sloc = _means_sloc['gh_sloc'].tolist()
        row_std_sloc = _std_sloc['gh_sloc'].tolist()

        matrix_means_code[idx][np.array(tuple(team_size))] = row_mean_code
        matrix_std_code[idx][np.array(tuple(team_size))] = row_std_code
        matrix_means_sloc[idx][np.array(tuple(team_size))] = row_mean_sloc
        matrix_std_sloc[idx][np.array(tuple(team_size))] = row_std_sloc

    total_mean_code = np.nanmean(matrix_means_code, axis=0)
    total_std_code = np.nanmean(matrix_std_code, axis=0)
    total_mean_sloc = np.nanmean(matrix_means_sloc, axis=0)
    total_std_sloc = np.nanmean(matrix_std_sloc, axis=0)

    total_mean = total_mean_code / total_mean_sloc
    total_std = total_std_code / total_std_sloc

    return total_mean, total_std


def line_plot():
    index = np.arange(means.shape[0])
    fig, ax = plt.subplot()
    ax.plot(index, means, marker='o', color='blueviolet', linewidth=1)
    ax.set_ylim(bottom=0.)
    plt.xlabel("Team size")
    plt.ylabel("Mean of source code diff")
    plt.legend()
    plt.savefig('figs/src_diff_ratio_line.png', dpi=500)
    plt.show()


def scatter_plot():
    index = np.arange(means.shape[0])
    plt.errorbar(index, means, std, linestyle='None', marker='_', lolims=True, elinewidth=0.5, ecolor='blueviolet',
                 capthick=0.5)
    plt.scatter(index, means, color='blueviolet', linewidth=0.5)
    plt.xlabel("Team size")
    plt.ylabel("Mean of source code diff over total size of project")
    plt.legend()
    plt.savefig('figs/src_diff_ratio_scatter.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    means, std = mean_std()
    scatter_plot()
    # line_plot()
