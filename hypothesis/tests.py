import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_csv("../sample/sample%s.csv" % j))


def median_tests():
    lower_half_mean_failed = []
    upper_half_mean_failed = []
    lower_half_mean_ok = []
    upper_half_mean_ok = []

    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')
        df.replace('', np.nan, inplace=True)
        df["tr_log_num_tests_failed"] = df["tr_log_num_tests_failed"].astype(float)
        df["tr_log_num_tests_ok"] = df["tr_log_num_tests_ok"].astype(float)
        df["tr_log_num_tests_run"] = df["tr_log_num_tests_run"].astype(float)

        _means_failed = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_failed'].mean()
        team_size = _means_failed['gh_team_size'].tolist()
        failed_list = _means_failed['tr_log_num_tests_failed'].tolist()
        index_pass = team_size.index(15)
        index_failed = team_size.index(5)
        _means_ok = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_ok'].mean()
        ok_list = _means_ok['tr_log_num_tests_ok'].tolist()
        _means_total = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_run'].mean()
        total_list = _means_total['tr_log_num_tests_run'].tolist()

        lower_half_mean_failed.append(np.mean(failed_list[:index_failed]) / np.mean(total_list[:index_failed]))
        upper_half_mean_failed.append(np.mean(failed_list[index_failed:]) / np.mean(total_list[index_failed:]))
        lower_half_mean_ok.append(np.mean(ok_list[:index_pass]) / np.mean(total_list[:index_pass]))
        upper_half_mean_ok.append(np.mean(ok_list[index_pass:]) / np.mean(total_list[index_pass:]))

    compare_failed = []
    compare_ok = []
    for a, b in zip(lower_half_mean_failed, upper_half_mean_failed):
        compare_failed.append(a - b)

    for a, b in zip(lower_half_mean_ok, upper_half_mean_ok):
        compare_ok.append(a - b)

    return compare_failed, compare_ok


def histogram_failure():
    sns.distplot(failure_difference, hist=True, kde=True,
                 bins=10, color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4}).set_title('Test failure ratio')

    plt.savefig('../figs2/test_failed_ratio.png', dpi=1000)
    plt.show()


def histogram_passed():
    sns.distplot(passed_difference, hist=True, kde=True,
                 bins=10, color='darkgreen',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4}).set_title('Test ok ratio')
    m = np.nanmean(passed_difference)
    s = np.nanstd(passed_difference)
    u = m + 3 * s
    l = m - 3 * s
    plt.axvline(x=m, color='red', linewidth=2)
    plt.axvline(x=u, color='red', linewidth=2)
    plt.axvline(x=l, color='red', linewidth=2)
    plt.savefig('../figs2/test_ok_ratio.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    failure_difference, passed_difference = median_tests()
    # histogram_failure()
    histogram_passed()
