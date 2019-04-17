import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# load the dataset
df = pd.read_csv('./refined.csv')

if not os.path.exists('figs'):
    os.makedirs('figs')

############################## RQ1 ##########################################
print("Number of unique projects are ", df['gh_project_name'].nunique(), "\n")

team_size = df.gh_team_size.unique()
# code changes
test_diff_ratio = np.array(df.groupby('gh_team_size', as_index=False)['test_diff_ratio'].mean()['test_diff_ratio'].tolist(), dtype=np.float)
src_diff_ratio = np.array(df.groupby('gh_team_size', as_index=False)['src_diff_ratio'].mean()['src_diff_ratio'].tolist(), dtype=np.float)

# tests
test_failed_ratio = np.array(df.groupby('gh_team_size', as_index=False)['test_failed_ratio'].mean()['test_failed_ratio'].tolist(), dtype=np.float)
test_ok_ratio = np.array(df.groupby('gh_team_size', as_index=False)['test_ok_ratio'].mean()['test_ok_ratio'].tolist(), dtype=np.float)

# date
date_diff = np.array(df.groupby('gh_team_size', as_index=False)['date_diff'].mean()['date_diff'].tolist(), dtype=np.float)
src_date = np.array(df.groupby('gh_team_size', as_index=False)['src_date'].mean()['src_date'].tolist(), dtype=np.float)
test_date = np.array(df.groupby('gh_team_size', as_index=False)['test_date'].mean()['test_date'].tolist(), dtype=np.float)

# Travis status
counts = df.groupby(['gh_team_size']).size().reset_index(name='counts')
failed = np.array(df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 0].tolist(), dtype=np.float)
passed = np.array(df.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 1].tolist(), dtype=np.float)
total_status = np.array(list(counts['counts']), dtype=np.float)

fig, ax = plt.subplots(2, 2)
ax[0, 0].boxplot(src_diff_ratio)
ax[0, 1].boxplot(test_diff_ratio)
ax[1, 0].boxplot(src_date)
ax[1, 1].boxplot(test_date)

ax[0, 0].set_xlabel('SCC ratio')
ax[0, 1].set_xlabel('TCC ratio')
ax[1, 0].set_xlabel('SCC ratio over time')
ax[1, 1].set_xlabel('TCC ratio over time')

plt.tight_layout(w_pad=0.5, h_pad=1.0)
plt.savefig('./figs/code_dist.eps', format='eps')

fig, ax = plt.subplots(2, 2)
ax[0, 0].boxplot(test_ok_ratio)
ax[0, 1].boxplot(test_failed_ratio)
ax[1, 0].boxplot(passed/total_status)
ax[1, 1].boxplot(failed/total_status)

ax[0, 0].set_xlabel('OK tests ratio')
ax[0, 1].set_xlabel('Failed tests ratio')
ax[1, 0].set_xlabel('Passed status ratio')
ax[1, 1].set_xlabel('Passed status ratio')
plt.tight_layout(w_pad=0.5, h_pad=1.0)
plt.savefig('./figs/rest_dist.eps', format='eps')

print("Correlation between team size and source code changes ratio")
print(stats.spearmanr(team_size, src_diff_ratio), "\n")
print("Correlation between team size and test code changes ratio")
print(stats.spearmanr(team_size, test_diff_ratio), "\n")
print("Correlation between team size and OK tests ratio")
print(stats.spearmanr(team_size, test_ok_ratio), "\n")
print("Correlation between team size and failed tests ratio")
print(stats.spearmanr(team_size, test_failed_ratio), "\n")
print("Correlation between team size and source code changes ratio over time")
print(stats.spearmanr(team_size, src_date), "\n")
print("Correlation between team size and test code changes ratio over time")
print(stats.spearmanr(team_size, test_date), "\n")
print("Correlation between team size and passed status ratio")
print(stats.spearmanr(team_size, failed/total_status), "\n")
print("Correlation between team size and failed status ratio")
print(stats.spearmanr(team_size, passed/total_status), "\n")

sample_set = 100

src_sloc = np.zeros((sample_set, len(team_size)))
test_sloc = np.zeros((sample_set, len(team_size)))
status_failed = np.zeros((sample_set, len(team_size)))
status_passed = np.zeros((sample_set, len(team_size)))
test_failed = np.zeros((sample_set, len(team_size)))
test_ok = np.zeros((sample_set, len(team_size)))
date = np.zeros((sample_set, len(team_size)))
src_date_res = np.zeros((sample_set, len(team_size)))
test_date_res = np.zeros((sample_set, len(team_size)))

# Here we create 100 sampel set from our dataset with replacement
for i in range(sample_set):
    sample = df.sample(frac=1, replace=True)
    sample = sample.sort_values('gh_team_size')

    # In each sample test each of the values for team sie from 0 to 60
    for index, threshold in enumerate(team_size):
        if index == 0 or index == len(team_size) - 1:
            continue

        # Calculate the mean of each feature for each team size
        src = sample.groupby('gh_team_size', as_index=False)['git_diff_src_churn'].mean()
        test = sample.groupby('gh_team_size', as_index=False)['git_diff_test_churn'].mean()
        sloc = sample.groupby('gh_team_size', as_index=False)['gh_sloc'].mean()
        counts = sample.groupby(['gh_team_size']).size().reset_index(name='counts')
        failed = sample.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 0].tolist()
        passed = sample.groupby(['gh_team_size']).tr_status.value_counts().unstack(fill_value=0).loc[:, 1].tolist()
        failed_tests = df.groupby('gh_team_size', as_index=False)['tr_log_num_tests_failed'].mean()
        ok_tests = sample.groupby('gh_team_size', as_index=False)['tr_log_num_tests_ok'].mean()
        total_tests = sample.groupby('gh_team_size', as_index=False)['tr_log_num_tests_run'].mean()
        date_diff = sample.groupby('gh_team_size', as_index=False)['date_diff'].mean()
        src_date = sample.groupby('gh_team_size', as_index=False)['src_date'].mean()
        test_date = sample.groupby('gh_team_size', as_index=False)['test_date'].mean()

        sloc_list = sloc['gh_sloc'].tolist()
        test_list = test['git_diff_test_churn'].tolist()
        src_list = src['git_diff_src_churn'].tolist()
        failed_tests_list = failed_tests['tr_log_num_tests_failed'].tolist()
        total_tests_list = total_tests['tr_log_num_tests_run'].tolist()
        ok_tests_list = ok_tests['tr_log_num_tests_ok'].tolist()
        date_diff_list = date_diff['date_diff'].tolist()
        src_date_list = src_date['src_date'].tolist()
        test_date_list = test_date['test_date'].tolist()
        total_status = list(counts['counts'])

        lower_half_mean_src = np.mean(src_list[:index]) / np.mean(sloc_list[:index])
        upper_half_mean_src = np.mean(src_list[index:]) / np.mean(sloc_list[index:])

        lower_half_mean_test = np.mean(test_list[:index]) / np.mean(sloc_list[:index])
        upper_half_mean_test = np.mean(test_list[index:]) / np.mean(sloc_list[index:])

        lower_half_mean_failure = np.mean(failed[:index]) / np.mean(total_status[:index])
        upper_half_mean_failure = np.mean(failed[index:]) / np.mean(total_status[index:])

        lower_half_mean_passed = np.mean(passed[:index]) / np.mean(total_status[:index])
        upper_half_mean_passed = np.mean(passed[index:]) / np.mean(total_status[index:])

        lower_half_failed_tests = np.mean(failed_tests_list[:index]) / np.mean(total_tests_list[:index])
        upper_half_failed_tests = np.mean(failed_tests_list[index:]) / np.mean(total_tests_list[index:])

        lower_half_ok_tests = np.mean(ok_tests_list[:index]) / np.mean(total_tests_list[:index])
        upper_half_ok_tests = np.mean(ok_tests_list[index:]) / np.mean(total_tests_list[index:])

        lower_half_date_diff = np.mean(date_diff_list[:index])
        upper_half_date_diff = np.mean(date_diff_list[index:])

        lower_half_src_date = np.mean(src_date_list[:index])
        upper_half_src_date = np.mean(src_date_list[index:])

        lower_half_test_date = np.mean(test_date_list[:index])
        upper_half_test_date = np.mean(test_date_list[index:])

        # Get the difference of mean from two side of the threshold
        src_sloc[i][index] = lower_half_mean_src - upper_half_mean_src
        test_sloc[i][index] = lower_half_mean_test - upper_half_mean_test
        status_failed[i][index] = lower_half_mean_failure - upper_half_mean_failure
        status_passed[i][index] = lower_half_mean_passed - upper_half_mean_passed
        test_failed[i][index] = lower_half_failed_tests - upper_half_failed_tests
        test_ok[i][index] = lower_half_ok_tests - upper_half_ok_tests
        date[i][index] = lower_half_date_diff - upper_half_date_diff
        src_date_res[i][index] = lower_half_src_date - upper_half_src_date
        test_date_res[i][index] = lower_half_test_date - upper_half_test_date

compare_src_sloc = src_sloc > 0
compare_test_sloc = test_sloc > 0
compare_status_failed = status_failed > 0
compare_status_passed = status_passed > 0
compare_test_failed = test_failed > 0
compare_test_ok = test_ok > 0
compare_date_dif = date > 0
compare_src_date = src_date_res > 0
compare_test_date = test_date_res > 0

sum_src_sloc = np.zeros(len(team_size))
sum_test_sloc = np.zeros(len(team_size))
sum_status_failed = np.zeros(len(team_size))
sum_status_passed = np.zeros(len(team_size))
sum_test_failed = np.zeros(len(team_size))
sum_test_ok = np.zeros(len(team_size))
sum_date_diff = np.zeros(len(team_size))
sum_src_date = np.zeros(len(team_size))
sum_test_date = np.zeros(len(team_size))
for i in range(len(team_size)):
    sum_src_sloc[i] = np.sum(compare_src_sloc[:, i])
    sum_test_sloc[i] = np.sum(compare_test_sloc[:, i])
    sum_status_failed[i] = np.sum(compare_status_failed[:, i])
    sum_status_passed[i] = np.sum(compare_status_passed[:, i])
    sum_test_failed[i] = np.sum(compare_test_failed[:, i])
    sum_test_ok[i] = np.sum(compare_test_ok[:, i])
    sum_date_diff[i] = np.sum(compare_date_dif[:, i])
    sum_src_date[i] = np.sum(compare_src_date[:, i])
    sum_test_date[i] = np.sum(compare_test_date[:, i])

mean_threshold = np.zeros(len(team_size))
for i in range(len(team_size)):
    mean_threshold[i] = np.mean(np.array([sum_src_sloc[i], sum_test_sloc[i], sum_status_failed[i], sum_status_passed[i], sum_test_failed[i], sum_test_ok[i], sum_src_date[i], sum_test_date[i]]))

selected = np.argmax(mean_threshold)
selected = 7
print("Team size threshold is ", selected, "\n")

############################## RQ2 ##########################################
temp = df.groupby(["gh_project_name", "gh_lang"], as_index=False).agg({'gh_team_size': 'mean'})
temp["gh_team_size"] = np.floor(temp["gh_team_size"])

crosstab = pd.crosstab(temp['gh_team_size'], temp['gh_lang'])
print(crosstab)

print("Number of projects in Ruby", crosstab['ruby'].sum())
print("Number of projects in Java", crosstab['java'].sum())
print("Number of projects in javascript", crosstab['javascript'].sum())

plt.plot(crosstab['ruby'])
plt.xlabel('team size')
plt.ylabel('Number of projects')
plt.savefig('./figs/ruby.eps', format='eps')

plt.plot(crosstab['java'])
plt.xlabel('team size')
plt.ylabel('Number of projects')
plt.savefig('./figs/java.eps', format='eps')

plt.plot(crosstab['javascript'])
plt.xlabel('team size')
plt.ylabel('Number of projects')
plt.savefig('./figs/javascript.eps', format='eps')
