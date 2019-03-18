import pandas as pd


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data/dummy%s.pkl" % j))


def commits():
    confidence1 = 0
    for df in data_frames:
        more_commit = 0  # > 5
        less_commit = 0  # <= 5
        for index, row in df.iterrows():
            team_size = int(df.at[index, 'gh_team_size'])
            if pd.notnull(df.at[index, 'gh_num_commits_in_push']):
                num_commit = int(df.at[index, 'gh_num_commits_in_push'])
                if team_size > 200:
                    if 2 < num_commit <= 5:
                        less_commit += 1
                    elif num_commit > 5:
                        more_commit += 1

        if less_commit > more_commit:
            confidence1 += 1

    print(confidence1)


if __name__ == '__main__':
    data_frames = []
    load_pkl()
    commits()
