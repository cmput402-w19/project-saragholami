import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("../data3/dummy%s.pkl" % j))


def mean_std():
    lower_half_mean_date = []
    upper_half_mean_date = []
    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        df['date_diff'] = df['gh_pushed_at'].sub(df['gh_first_commit_created_at'], axis=0)  # timedelta64[ns] type
        df["date_diff"] = df["date_diff"] / np.timedelta64(1, 'm')

        _means = df.groupby('gh_team_size', as_index=False)['date_diff'].mean()
        team_size = _means['gh_team_size'].tolist()
        date_list = _means['date_diff'].tolist()
        index = math.floor(len(team_size) / 2)

        lower_half_mean_date.append(np.mean(date_list[:index]))
        upper_half_mean_date.append(np.mean(date_list[index:]))

    compare_date = []
    for a, b in zip(lower_half_mean_date, upper_half_mean_date):
        compare_date.append(a - b)

    return compare_date


# def line_plot():
#     index = np.arange(means.shape[0])
#     fig, ax = plt.subplots()
#     ax.plot(index, means, marker='o', color='purple', linewidth=1)
#     plt.xlabel("Team size")
#     plt.ylabel("Date diff")
#     plt.legend()
#     plt.savefig('figs/date_diff_line.png', dpi=1000)
#     plt.show()
#
#
# def scatter_plot():
#     index = np.arange(means.shape[0])
#     plt.errorbar(index, means, std, linestyle='None', marker='_', lolims=True, elinewidth=0.5, ecolor='purple',
#                  capthick=0.5)
#     plt.scatter(index, means, color='crimson', linewidth=0.5)
#     plt.xlabel("Team size")
#     plt.ylabel("Date diff")
#     plt.legend()
#     plt.savefig('figs/date_diff_scatter.png', dpi=1000)
#     plt.show()

def histogram_date():
    sns.distplot(date, hist=True, kde=True,
                 bins=10, color='darkgreen',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    date = mean_std()
    histogram_date()
    # line_plot()
    # scatter_plot()
