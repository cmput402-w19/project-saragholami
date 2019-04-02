import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_csv("../sample/sample%s.csv" % j))


def mean_std():
    lower_half_mean = []
    upper_half_mean = []

    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        _means_src = df.groupby('gh_team_size', as_index=False)['test_date'].mean()

        team_size = _means_src['gh_team_size'].tolist()
        test_list = _means_src['test_date'].tolist()

        index = team_size.index(8)

        lower_half_mean.append(np.mean(test_list[:index]))
        upper_half_mean.append(np.mean(test_list[index:]))

    compare_src = []
    for a, b in zip(lower_half_mean, upper_half_mean):
        compare_src.append(a - b)

    return compare_src


def histogram():
    sns.distplot(diff, hist=True, kde=True,
                 bins=15, color='purple',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Test code changes over time interval')
    m = np.nanmean(diff)
    s = np.nanstd(diff)
    u = m + 2 * s
    l = m - 2 * s
    plt.axvline(x=m, color='red', linewidth=2)
    plt.axvline(x=u, color='red', linewidth=2)
    plt.axvline(x=l, color='red', linewidth=2)
    plt.savefig('../figs2/test_date.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    diff = mean_std()
    histogram()
