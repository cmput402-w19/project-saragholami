import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data3/dummy%s.pkl" % j))


def mean_std():
    matrix_failure = np.zeros((100, 60))
    matrix_pass = np.zeros((100, 60))
    for idx, df in enumerate(data_frames):
        team_size = df.gh_team_size.unique()
        failed = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 'failed'].tolist()
        errored = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 'errored'].tolist()
        passed = df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 'passed'].tolist()
        failure = [x + y for x, y in zip(failed, errored)]
        matrix_failure[idx][np.array(tuple(team_size))] = failure
        matrix_pass[idx][np.array(tuple(team_size))] = passed

    total_failure = np.nanmean(matrix_failure, axis=0)
    total_pass = np.nanmean(matrix_pass, axis=0)
    return total_failure, total_pass


def line_plot():
    index = np.arange(fails.shape[0])
    fig, ax = plt.subplots()
    ax.plot(index, fails, marker='o', color='darkorchid', linewidth=1, label="Failed/Errored builds")
    ax.plot(index, passes, marker='o', color='yellowgreen', linewidth=1, label="Passed builds")
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Team size", fontsize=18)
    plt.ylabel("Travis status", fontsize=18)
    fig.suptitle('Travis Build Status', fontsize=20)
    plt.legend()
    plt.savefig('figs/status_line.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    fails, passes = mean_std()
    # scatter_plot()
    line_plot()
