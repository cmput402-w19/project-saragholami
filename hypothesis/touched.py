import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_csv("../sample/sample%s.csv" % j))


def mean_std():
    lower_half_mean_touched = []
    upper_half_mean_touched = []

    for idx, df in enumerate(data_frames):
        df = df.sort_values('gh_team_size')

        _means_src = df.groupby('gh_team_size', as_index=False)['gh_num_commits_on_files_touched'].mean()

        team_size = _means_src['gh_team_size'].tolist()
        src_list = _means_src['gh_num_commits_on_files_touched'].tolist()

        index = team_size.index(15)

        lower_half_mean_touched.append(np.mean(src_list[:index]))
        upper_half_mean_touched.append(np.mean(src_list[index:]))

    compare_src = []
    for a, b in zip(lower_half_mean_touched, upper_half_mean_touched):
        compare_src.append(a - b)

    return compare_src


def histogram():
    sns.distplot(touched, hist=True, kde=True,
                 bins=15, color='green',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 3}).set_title('Number of unique commits on the files touched in the commits')
    plt.savefig('../figs2/touched.png', dpi=1000)
    plt.show()


if __name__ == '__main__':
    data_frames = []
    load_pkl()

    touched = mean_std()
    histogram()
