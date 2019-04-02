import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
    Threshold for team size is 15 where the histogram is on one side of X axis.
"""


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_csv("../sample/sample%s.csv" % j))


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

        index = team_size.index(20)

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


def histogram_src():
    sns.distplot(src, hist=True, kde=True,
                 bins=15, color='c',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Source code changes over total project')
    m = np.nanmean(src)
    s = np.nanstd(src)
    u = m + 2 * s
    l = m - 2 * s
    plt.axvline(x=m, color='red', linewidth=2)
    plt.axvline(x=u, color='red', linewidth=2)
    plt.axvline(x=l, color='red', linewidth=2)
    plt.savefig('../figs2/src_diff_ratio.png', dpi=1000)
    plt.show()


def histogram_test():
    sns.distplot(test, hist=True, kde=True,
                 bins=15, color='darkmagenta',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Test code changes over total project')
    m = np.nanmean(test)
    s = np.nanstd(test)
    u = m + 2 * s
    l = m - 2 * s
    plt.axvline(x=m, color='b', linewidth=2)
    plt.axvline(x=u, color='b', linewidth=2)
    plt.axvline(x=l, color='b', linewidth=2)
    plt.savefig('../figs2/test_diff_ratio.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    src, test = mean_std()
    histogram_src()
    histogram_test()
