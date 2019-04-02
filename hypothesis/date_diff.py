import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_csv("../sample/sample%s.csv" % j))


def mean_std():
    lower_half_mean_date = []
    upper_half_mean_date = []
    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        _means = df.groupby('gh_team_size', as_index=False)['date_diff'].mean()
        team_size = _means['gh_team_size'].tolist()
        date_list = _means['date_diff'].tolist()

        index = team_size.index(5)

        lower_half_mean_date.append(np.mean(date_list[:index]))
        upper_half_mean_date.append(np.mean(date_list[index:]))

    compare_date = []
    for a, b in zip(lower_half_mean_date, upper_half_mean_date):
        compare_date.append(a - b)

    return compare_date


def histogram():
    sns.distplot(date, hist=True, kde=True,
                 bins=15, color='darkgreen',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Interval between first commit created and pushed')
    plt.savefig('../figs2/date_diff.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    date = mean_std()
    histogram()
