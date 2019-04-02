import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_csv("../sample/sample%s.csv" % j))


def mean_std():
    lower_half_mean_failure = []
    upper_half_mean_failure = []
    lower_half_mean_passed = []
    upper_half_mean_passed = []

    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        team_size = df.gh_team_size.unique()
        index = np.where(team_size == 15)[0][0]
        counts = df.groupby(['gh_team_size']).size().reset_index(name='counts')
        total = list(counts['counts'])
        failed = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 0].tolist()
        passed = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 1].tolist()

        lower_half_mean_failure.append(np.mean(failed[:index]) / np.mean(total[:index]))
        upper_half_mean_failure.append(np.mean(failed[index:]) / np.mean(total[index:]))

        lower_half_mean_passed.append(np.mean(passed[:index]) / np.mean(total[:index]))
        upper_half_mean_passed.append(np.mean(passed[index:]) / np.mean(total[index:]))

    compare_failure = []
    compare_passed = []
    for a, b in zip(lower_half_mean_failure, upper_half_mean_failure):
        compare_failure.append(a - b)

    for a, b in zip(lower_half_mean_passed, upper_half_mean_passed):
        compare_passed.append(a - b)
    return compare_failure, compare_passed


def histogram_failure():
    sns.distplot(failure_difference, hist=True, kde=True,
                 bins=10, color='darkred',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Build status failure')
    m = np.nanmean(failure_difference)
    s = np.nanstd(failure_difference)
    u = m + 3 * s
    l = m - 3 * s
    plt.axvline(x=m, color='green', linewidth=2)
    plt.axvline(x=u, color='green', linewidth=2)
    plt.axvline(x=l, color='green', linewidth=2)
    plt.savefig('../figs2/status_failed.png', dpi=1000)
    plt.show()


def histogram_passed():
    sns.distplot(passed_difference, hist=True, kde=True,
                 bins=10, color='darkgreen',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Build status pass')
    m = np.nanmean(passed_difference)
    s = np.nanstd(passed_difference)
    u = m + 3 * s
    l = m - 3 * s
    plt.axvline(x=m, color='red', linewidth=2)
    plt.axvline(x=u, color='red', linewidth=2)
    plt.axvline(x=l, color='red', linewidth=2)
    plt.savefig('../figs2/status_passed.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    failure_difference, passed_difference = mean_std()
    histogram_passed()
    histogram_failure()
