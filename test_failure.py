import pandas as pd


def load_pkl():
    for j in range(1):
        data_frames.append(pd.read_pickle("./data/dummy%s.pkl" % j))


def calculate_failure_rate():
    for df in data_frames:
        if 'failure_rate' not in df:
            df['failure_rate'] = 0

        fail = pd.notnull(df["tr_log_num_tests_failed"])
        run = pd.notnull(df["tr_log_num_tests_run"])
        for index, row in df.iterrows():
            if fail[index] and run[index] and df.at[index, 'tr_log_num_tests_failed'] is not "" and df.at[index, 'tr_log_num_tests_run'] is not "":
                df.at[index, 'failure_rate'] = float(df.loc[index, 'tr_log_num_tests_failed']) / float(
                    df.loc[index, 'tr_log_num_tests_run'])


if __name__ == '__main__':
    data_frames = []
    load_pkl()
    calculate_failure_rate()
