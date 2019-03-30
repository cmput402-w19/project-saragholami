import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_pkl():
    for j in range(1):
        data_frames.append(pd.read_pickle("./data3/dummy%s.pkl" % j))


def mean_std():
    matrix_means = np.zeros((100, 60))
    matrix_std = np.zeros((100, 60))
    for idx, df in enumerate(data_frames):
        print(df.dtypes)
        df['date_diff'] = df['gh_pushed_at'].sub(df['gh_first_commit_created_at'], axis=0)  # timedelta64[ns] type
        df["date_diff"] = df["date_diff"] / np.timedelta64(1, 'm')
        _means = df.groupby('gh_team_size', as_index=False)['date_diff'].mean()
        _std = df.groupby('gh_team_size', as_index=False)['date_diff'].std()
        team_size = _means['gh_team_size'].tolist()
        row_mean = _means['date_diff'].tolist()
        row_std = _std['date_diff'].tolist()
        matrix_means[idx][np.array(tuple(team_size))] = row_mean
        matrix_std[idx][np.array(tuple(team_size))] = row_std

    total_mean = np.nanmean(matrix_means, axis=0)
    total_std = np.nanmean(matrix_std, axis=0)
    return total_mean, total_std


def line_plot():
    index = np.arange(means.shape[0])
    fig, ax = plt.subplots()
    ax.plot(index, means, marker='o', color='purple', linewidth=1)
    plt.xlabel("Team size")
    plt.ylabel("Date diff")
    plt.legend()
    plt.savefig('figs/date_diff_line.png', dpi=1000)
    plt.show()


def scatter_plot():
    index = np.arange(means.shape[0])
    plt.errorbar(index, means, std, linestyle='None', marker='_', lolims=True, elinewidth=0.5, ecolor='purple',
                 capthick=0.5)
    plt.scatter(index, means, color='crimson', linewidth=0.5)
    plt.xlabel("Team size")
    plt.ylabel("Date diff")
    plt.legend()
    plt.savefig('figs/date_diff_scatter.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    means, std = mean_std()
    line_plot()
    scatter_plot()
