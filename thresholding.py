import pandas as pd
import numpy as np

df = pd.read_csv('D://CMPUT501/project/project-saragholami/sample/travis_torrent_refined.csv')
df = df.sort_values('gh_team_size')

team_size = df.gh_team_size.unique()
diff = np.zeros(team_size)

for index, threshold in enumerate(team_size):
    if index == 0 or index == len(team_size) - 1:
        continue

    src = df.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].mean()
    sloc = df.groupby('gh_team_size', as_index=False)['gh_sloc'].mean()

    sloc_list = sloc['gh_sloc'].tolist()
    src_list = src['git_diff_src_churn'].tolist()

    lower_half_mean_src = np.mean(src_list[:index]) / np.mean(sloc_list[:index])
    upper_half_mean_src = np.mean(src_list[index:]) / np.mean(sloc_list[index:])

    diff[index] = lower_half_mean_src - upper_half_mean_src


