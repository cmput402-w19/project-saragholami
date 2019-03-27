import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data3/dummy%s.pkl" % j))


def code_mean():
    matrix_means_failed = np.zeros((100, 60))
    matrix_std_failed = np.zeros((100, 60))
    matrix_means_ok = np.zeros((100, 60))
    matrix_std_ok = np.zeros((100, 60))
    matrix_means_total = np.zeros((100, 60))
    matrix_std_total = np.zeros((100, 60))
    for idx, df in enumerate(data_frames):
        df.replace('', np.nan, inplace=True)
        df["tr_log_num_tests_failed"] = df["tr_log_num_tests_failed"].astype(float)
        df["tr_log_num_tests_ok"] = df["tr_log_num_tests_ok"].astype(float)
        df["tr_log_num_tests_run"] = df["tr_log_num_tests_run"].astype(float)

        _means_failed = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_failed'].mean()
        _std_failed = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_failed'].std()
        team_size = _means_failed['gh_team_size'].tolist()
        row_mean_failed = _means_failed['tr_log_num_tests_failed'].tolist()
        row_std_failed = _std_failed['tr_log_num_tests_failed'].tolist()
        matrix_means_failed[idx][np.array(tuple(team_size))] = row_mean_failed
        matrix_std_failed[idx][np.array(tuple(team_size))] = row_std_failed

        _means_ok = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_ok'].mean()
        _std_ok = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_ok'].std()
        row_mean_ok = _means_ok['tr_log_num_tests_ok'].tolist()
        row_std_ok = _std_ok['tr_log_num_tests_ok'].tolist()
        matrix_means_ok[idx][np.array(tuple(team_size))] = row_mean_ok
        matrix_std_ok[idx][np.array(tuple(team_size))] = row_std_ok

        _means_total = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_run'].mean()
        _std_total = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_run'].std()
        row_mean_total = _means_total['tr_log_num_tests_run'].tolist()
        row_std_total = _std_total['tr_log_num_tests_run'].tolist()
        matrix_means_total[idx][np.array(tuple(team_size))] = row_mean_total
        matrix_std_total[idx][np.array(tuple(team_size))] = row_std_total

    total_mean_failed = np.nanmean(matrix_means_failed, axis=0)
    total_std_failed = np.nanmean(matrix_std_failed, axis=0)

    total_mean_ok = np.nanmean(matrix_means_ok, axis=0)
    total_std_ok = np.nanmean(matrix_std_ok, axis=0)

    total_mean_total = np.nanmean(matrix_means_total, axis=0)
    total_std_total = np.nanmean(matrix_std_total, axis=0)
    return total_mean_failed, total_std_failed, total_mean_ok, total_std_ok, total_mean_total, total_std_total


def line_plot():
    index = np.arange(means_failed.shape[0])
    plt.plot(index, means_ok, marker='o', color='green', linewidth=1, label="Passed tests")
    plt.plot(index, means_total, marker='o', color='blue', linewidth=1, label="Total tests")
    plt.plot(index, means_failed, marker='o', color='red', linewidth=1, label="Failed tests")
    plt.xlabel("Team size")
    plt.ylabel("Number of tests")
    plt.legend()
    plt.savefig('figs/tests_line.png', dpi=500)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    means_failed, std_failed, means_ok, std_ok, means_total, std_total = code_mean()
    line_plot()
