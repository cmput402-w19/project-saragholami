import pandas as pd
import numpy as np


def preprocess():
    df = pd.read_csv('D://CMPUT501/project/project-saragholami/csv/travistorrent_8_2_2017.csv')
    # Getting project with team size below 60
    df = df.loc[df['gh_team_size'] < 60]
    # Dropping useless columns
    df = df.drop(
        ["tr_build_id", "tr_job_id", "tr_build_number", "git_branch", "gh_is_pr", "git_merged_with", "gh_pull_req_num",
         "gh_commits_in_push", "git_prev_commit_resolution_status", "git_prev_built_commit", "tr_prev_build",
         "git_all_built_commits", "git_trigger_commit", "tr_virtual_merged_into", "tr_original_commit", "tr_jobs"],
        axis=1)
    # Convert gh_pushed_at and gh_first_commit_created_at to delta time
    df['gh_pushed_at'] = pd.to_datetime(df['gh_pushed_at'])
    df['gh_first_commit_created_at'] = pd.to_datetime(df['gh_first_commit_created_at'])
    # Get date diff from them
    df['date_diff'] = df['gh_pushed_at'].sub(df['gh_first_commit_created_at'], axis=0)
    df["date_diff"] = df["date_diff"] / np.timedelta64(1, 'm')
    # Map gh_by_core_team_member to 0 and 1
    df['gh_by_core_team_member'] = df['gh_by_core_team_member'].map({True: 1, False: 0})
    # Dropping rows where travis status is canceled or started and mapping the rest to 0 and 1
    df = df[df.tr_status != 'canceled']
    df = df[df.tr_status != 'started']
    df['tr_status'] = df['tr_status'].map({'passed': 1, 'failed': 0, 'errored': 0})
    # Source and test code ratio and their ratio over time
    df["src_diff_ratio"] = df["git_diff_src_churn"] / df["gh_sloc"]
    df["src_date"] = df["src_diff_ratio"] / df["date_diff"]
    df["test_diff_ratio"] = df["git_diff_test_churn"] / df["gh_sloc"]
    df["test_date"] = df["test_diff_ratio"] / df["date_diff"]
    df = df.replace([np.inf, -np.inf], np.nan)
    # Save data frame to pickle file
    df.to_pickle("D://CMPUT501/project/project-saragholami/pickle/travis_torrent.pkl")


def subsample():
    df = pd.read_pickle("./pickle/travis_torrent.pkl")
    for i in range(100):
        df_sample = df.sample(10000)
        df_sample.to_csv("./sample/sample%s.csv" % i)


if __name__ == '__main__':
    preprocess()
    # subsample()
