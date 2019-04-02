import pandas as pd

"""
    Significance. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
"""


def significance(p_value):
    if 0 <= p_value <= 0.001:
        print("*** ", p_value)
    elif 0.001 < p_value <= 0.01:
        print("** ", p_value)
    elif 0.01 < p_value <= 0.05:
        print("* ", p_value)
    elif 0.05 < p_value <= 0.1:
        print(". ", p_value)
    elif 0.1 < p_value <= 1:
        print(" ", p_value)


df = pd.read_csv('./models/src_code_diff.txt', sep=" ")
src = df['p-value'].mean()
print("Source code change ratio:")
significance(src)

df = pd.read_csv('./models/test_code_diff.txt', sep=" ")
test = df['p-value'].mean()
print("Test code change ratio:")
significance(test)

df = pd.read_csv('./models/assert.txt', sep=" ")
num_assert = df['p-value'].mean()
print("Assert:")
significance(num_assert)

df = pd.read_csv('./models/core.txt', sep=" ")
core = df['p-value'].mean()
print("Core:")
significance(core)

df = pd.read_csv('./models/date_diff.txt', sep=" ")
date_diff = df['p-value'].mean()
print("Date Diff:")
significance(date_diff)

df = pd.read_csv('./models/status.txt', sep=" ")
status = df['p-value'].mean()
print("Status:")
significance(status)

df = pd.read_csv('./models/num_commits.txt', sep=" ")
num_commits = df['p-value'].mean()
print("Number of Commits:")
significance(num_commits)

df = pd.read_csv('./models/test_failed.txt', sep=" ")
test_failed = df['p-value'].mean()
print("Test Failed:")
significance(test_failed)

df = pd.read_csv('./models/test_ok.txt', sep=" ")
test_ok = df['p-value'].mean()
print("Test OK:")
significance(test_ok)

df = pd.read_csv('./models/test_run.txt', sep=" ")
test_run = df['p-value'].mean()
print("Test Run:")
significance(test_run)

df = pd.read_csv('./models/failed_ratio.txt', sep=" ")
failed_ratio = df['p-value'].mean()
print("Failed Ratio:")
significance(failed_ratio)

df = pd.read_csv('./models/ok_ratio.txt', sep=" ")
ok_ratio = df['p-value'].mean()
print("OK Ratio:")
significance(ok_ratio)

df = pd.read_csv('./models/touched.txt', sep=" ")
touched = df['p-value'].mean()
print("Touched Files:")
significance(touched)

df = pd.read_csv('./models/test_line.txt', sep=" ")
test_line = df['p-value'].mean()
print("Test Lines:")
significance(test_line)

df = pd.read_csv('./models/test_case.txt', sep=" ")
test_case = df['p-value'].mean()
print("Test Cases:")
significance(test_case)

df = pd.read_csv('./models/sloc.txt', sep=" ")
sloc = df['p-value'].mean()
print("Sloc:")
significance(sloc)
