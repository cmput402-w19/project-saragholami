import pandas as pd


def load_pkl():
    for j in range(100):
        data_frames.append(pd.read_pickle("./data/dummy%s.pkl" % j))


def diff_less_50():
    confidence = 0
    for df in data_frames:
        more_change = 0  # > 5
        less_change = 0  # <= 5
        for index, row in df.iterrows():
            team_size = int(df.at[index, 'gh_team_size'])
            if pd.notnull(df.at[index, 'git_diff_src_churn']):
                code_diff = int(df.at[index, 'git_diff_src_churn'])
                if team_size < 50:
                    if code_diff < 25:
                        less_change += 1
                    else:
                        more_change += 1

        if less_change > more_change:
            confidence += 1

    print("0-50", confidence)


def between_50_100():
    confidence = 0
    for df in data_frames:
        more_change = 0  # > 5
        less_change = 0  # <= 5
        for index, row in df.iterrows():
            team_size = int(df.at[index, 'gh_team_size'])
            if pd.notnull(df.at[index, 'git_diff_src_churn']):
                code_diff = int(df.at[index, 'git_diff_src_churn'])
                if 50 < team_size < 120:
                    if code_diff < 25:
                        less_change += 1
                    else:
                        more_change += 1

        if less_change > more_change:
            confidence += 1

    print("50-100 ", confidence)


def over_200():
    confidence = 0
    for df in data_frames:
        more_change = 0  # > 5
        less_change = 0  # <= 5
        for index, row in df.iterrows():
            team_size = int(df.at[index, 'gh_team_size'])
            if pd.notnull(df.at[index, 'git_diff_src_churn']):
                code_diff = int(df.at[index, 'git_diff_src_churn'])
                if team_size > 190:
                    if code_diff < 25:
                        less_change += 1
                    else:
                        more_change += 1

        if less_change > more_change:
            confidence += 1

    print("> 190 ", confidence)


if __name__ == '__main__':
    data_frames = []
    load_pkl()
    diff_less_50()  # 100
    between_50_100()  # 87
    over_200()  # 100
