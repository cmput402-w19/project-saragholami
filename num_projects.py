import matplotlib.pyplot as plt
import pandas as pd
#
# project_num = np.zeros(101)
#
#
# def read_csv():
#     with open('num_projects2.csv', 'r') as csv_file:
#         plots = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in plots:
#             if line_count != 0:
#                 project_num[int(row[0])] = float(row[1])
#                 line_count += 1
#             else:
#                 line_count += 1
#
#

#
#
# if __name__ == '__main__':
#     read_csv()
#     line_plot()

project_num = []
team_size = []


def load_pkl():
    global project_num, team_size
    df = pd.read_pickle("./data2/project_num.pkl")
    team_size = df['gh_team_size'].tolist()
    project_num = df['project_count'].tolist()


def line_plot():
    # index = np.arange(101)
    plt.plot(team_size, project_num, color='green', linewidth=1)
    plt.xlabel("Team size")
    plt.ylabel("Number of projects")
    plt.legend()
    plt.savefig('figs/project_num_line.png', dpi=500)
    plt.show()


if __name__ == '__main__':
    # Open database connection

    load_pkl()
    line_plot()

    # disconnect from server
