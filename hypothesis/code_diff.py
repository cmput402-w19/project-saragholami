import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("../data3/dummy%s.pkl" % j))


def mean_std():
    lower_half_mean_src = []
    upper_half_mean_src = []
    lower_half_mean_test = []
    upper_half_mean_test = []

    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        _means_src = df.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].mean()
        _means_sloc = df.groupby('gh_team_size', as_index=False)['gh_sloc'].mean()
        _means_test = df.groupby('gh_team_size', as_index=False)['git_diff_test_churn'].mean()

        team_size = _means_src['gh_team_size'].tolist()
        src_list = _means_src['git_diff_src_churn'].tolist()
        sloc_list = _means_sloc['gh_sloc'].tolist()
        test_list = _means_test['git_diff_test_churn'].tolist()

        index = math.floor(len(team_size) / 2)

        lower_half_mean_src.append(np.mean(src_list[:index]) / np.mean(sloc_list[:index]))
        upper_half_mean_src.append(np.mean(src_list[index:]) / np.mean(sloc_list[index:]))
        lower_half_mean_test.append(np.mean(test_list[:index]) / np.mean(sloc_list[:index]))
        upper_half_mean_test.append(np.mean(test_list[index:]) / np.mean(sloc_list[index:]))

    compare_src = []
    compare_test = []
    for a, b in zip(lower_half_mean_src, upper_half_mean_src):
        compare_src.append(a - b)

    for a, b in zip(lower_half_mean_test, upper_half_mean_test):
        compare_test.append(a - b)

    return compare_src, compare_test


# def line_plot():
#     index = np.arange(means.shape[0])
#     fig, ax = plt.subplot()
#     ax.plot(index, means, marker='o', color='crimson', linewidth=1)
#     ax.set_ylim(bottom=0.)
#     plt.xlabel("Team size")
#     plt.ylabel("Mean of source code diff")
#     plt.legend()
#     plt.savefig('figs/src_diff_line.png', dpi=500)
#     plt.show()
#
#
# def scatter_plot():
#     index = np.arange(means.shape[0])
#     plt.errorbar(index, means, std, linestyle='None', marker='_', lolims=True, elinewidth=0.5, ecolor='crimson',
#                  capthick=0.5)
#     plt.scatter(index, means, color='crimson', linewidth=0.5)
#     plt.xlabel("Team size")
#     plt.ylabel("Mean of source code diff")
#     plt.legend()
#     plt.savefig('figs/src_diff_scatter.png', dpi=1000)
#     plt.show()

def histogram_src():
    sns.distplot(src, hist=True, kde=True,
                 bins=10, color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.show()


def histogram_test():
    sns.distplot(test, hist=True, kde=True,
                 bins=10, color='pink',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    src, test = mean_std()
    histogram_src()
    histogram_test()
    # scatter_plot()
    # line_plot()
