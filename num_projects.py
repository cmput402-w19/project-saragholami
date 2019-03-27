import matplotlib.pyplot as plt
import pandas as pd

project_num = []
team_size = []


def load_pkl():
    global project_num, team_size
    df = pd.read_pickle("./data3/project_num.pkl")
    team_size = df['gh_team_size'].tolist()
    project_num = df['project_count'].tolist()


def line_plot():
    plt.plot(team_size, project_num, color='green', linewidth=1)
    plt.xlabel("Team size")
    plt.ylabel("Number of projects")
    plt.legend()
    plt.savefig('figs/project_num_line.png', dpi=500)
    plt.show()


if __name__ == '__main__':

    load_pkl()
    line_plot()
