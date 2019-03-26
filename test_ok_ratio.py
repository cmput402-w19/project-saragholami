import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data3/dummy%s.pkl" % j))


def code_mean():
    matrix_means_ok = np.zeros((100, 60))
    matrix_std_ok = np.zeros((100, 60))
    matrix_means_total = np.zeros((100, 60))
    matrix_std_total = np.zeros((100, 60))

    for idx, df in enumerate(data_frames):
        df.replace('', np.nan, inplace=True)
        df["tr_log_num_tests_ok"] = df["tr_log_num_tests_ok"].astype(float)
        df["tr_log_num_tests_run"] = df["tr_log_num_tests_run"].astype(float)

        _means_ok = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_ok'].mean()
        _std_ok = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_ok'].std()
        team_size = _means_ok['gh_team_size'].tolist()
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

    total_mean_ok = np.nanmean(matrix_means_ok, axis=0)
    total_std_ok = np.nanmean(matrix_std_ok, axis=0)

    total_mean_total = np.nanmean(matrix_means_total, axis=0)
    total_std_total = np.nanmean(matrix_std_total, axis=0)

    total_mean = total_mean_ok / total_mean_total
    total_std = total_std_ok / total_std_total
    return total_mean, total_std


def line_plot():
    index = np.arange(means.shape[0])
    plt.plot(index, means, marker='o', color='limegreen', linewidth=1)
    plt.xlabel("Team size")
    plt.ylabel("Tests Success Ratio")
    plt.legend()
    plt.savefig('figs/successful_test_ratio_line.png', dpi=500)
    plt.show()


def scatter_plot():
    index = np.arange(means.shape[0])
    plt.errorbar(index, means, std, linestyle='None', marker='_', lolims=True, elinewidth=0.5, ecolor='limegreen',
                 capthick=0.5)
    plt.scatter(index, means, color='lime', linewidth=0.5)
    plt.xlabel("Team size")
    plt.ylabel("Tests Success Ratio")
    plt.legend()
    plt.savefig('figs/successful_test_ratio_scatter.png', dpi=500)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    means, std = code_mean()
    scatter_plot()
    # line_plot()
