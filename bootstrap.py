import MySQLdb
import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql


def subsample():
    query = "SELECT id FROM travistorrent_8_2_2017 WHERE gh_team_size < 60"
    df = psql.read_sql(query, con=db)
    # num_rows = 3702595
    list_of_id = df['id'].tolist()
    num_rows = len(list_of_id)
    # print("number of rows ", num_rows)
    for j in range(100):
        ids = []
        for i in range(3000000):
            index = random.randint(0, num_rows - 1)
            # print index
            # print list_of_id[index]
            ids.append(list_of_id[index])

        in_p = ', '.join(list(map(lambda x: '%s', ids)))
        query = "SELECT * FROM travistorrent_8_2_2017 WHERE ID IN (%s)"
        query = query % in_p
        df = psql.read_sql(query, params=ids, con=db)
        df.to_pickle("./data2/dummy%s.pkl" % j)


def load_pkl():
    for j in range(100):
        data.append(pd.read_pickle("./data2/dummy%s.pkl" % j))


def get_data():
    query = "SELECT gh_team_size, COUNT(DISTINCT gh_project_name) AS project_count FROM travistorrent_8_2_2017 " \
            "GROUP BY gh_team_size ORDER BY gh_team_size"
    df = psql.read_sql(query, con=db)
    df.to_pickle("./data2/project_num.pkl")


if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "", "travistorrent")

    subsample()
    data = []
    load_pkl()

    # get_data()
    # disconnect from server
    db.close()
