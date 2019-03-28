import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("../data3/dummy%s.pkl" % j))


def mean_std():
    lower_half_mean_failure = []
    upper_half_mean_failure = []
    lower_half_mean_passed = []
    upper_half_mean_passed = []

    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        team_size = df.gh_team_size.unique()
        index = math.floor(len(team_size) / 2)  # median index
        counts = df.groupby(['gh_team_size']).size().reset_index(name='counts')
        total = list(counts['counts'])
        failed = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 'failed'].tolist()
        errored = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 'errored'].tolist()
        passed = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 'passed'].tolist()
        failure = [x + y for x, y in zip(failed, errored)]

        lower_half_mean_failure.append(np.mean(failure[:index]) / np.mean(total[:index]))
        upper_half_mean_failure.append(np.mean(failure[index:]) / np.mean(total[index:]))

        lower_half_mean_passed.append(np.mean(passed[:index]) / np.mean(total[:index]))
        upper_half_mean_passed.append(np.mean(passed[index:]) / np.mean(total[index:]))

    compare_failure = []
    compare_passed = []
    for a, b in zip(lower_half_mean_failure, upper_half_mean_failure):
        compare_failure.append(a - b)

    for a, b in zip(lower_half_mean_passed, upper_half_mean_passed):
        compare_passed.append(a - b)
    return compare_failure, compare_passed  # mean : (-0.18471455453527175, 0.19370535216223356)


def histogram_failure():
    sns.distplot(failure_difference, hist=True, kde=True,
                 bins=10, color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.show()


def histogram_passed():
    sns.distplot(passed_difference, hist=True, kde=True,
                 bins=10, color='darkgreen',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    failure_difference, passed_difference = mean_std()
    histogram_passed()
    histogram_failure()
