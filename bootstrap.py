import MySQLdb
import random
import pandas as pd
import pandas.io.sql as psql


def subsample():
    num_rows = 3702595
    for j in range(100):
        ids = []
        for i in range(1000):
            index = random.randint(1, num_rows + 1)
            ids.append(index)

        in_p = ', '.join(list(map(lambda x: '%s', ids)))
        query = "SELECT * FROM travistorrent_8_2_2017 WHERE ID IN (%s)"
        query = query % in_p
        df = psql.read_sql(query, params=ids, con=db)
        df.to_pickle("./data/dummy%s.pkl" % j)


def load_pkl():
    for j in range(100):
        data.append(pd.read_pickle("./data/dummy%s.pkl" % j))


if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "", "travistorrent")

    subsample()
    data = []
    load_pkl()

    # disconnect from server
    db.close()
