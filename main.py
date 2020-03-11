#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run command ./main.py > test


# import MySQLdb
import pymysql
server = "localhost"
user_name = "projectUser"
password = "projectUser!@3"
db_name = "Georgian_Words"
query = "select * from correct_words limit 50 "


def connect_mysqldb(query):
    try:
        # db = MySQLdb.connect(server, user_name, password, db_name, charset='utf8')
        db = pymysql.connect(server, user_name, password,
                             db_name, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    except Exception as ex:
        print(ex)

    cr = db.cursor()
    cr.execute(query)
    # need to fix, fetch tuple type but we need dictionary
    data = cr.fetchall()
    print(type(data))
    print(data)
    db.close()


if __name__ == "__main__":
    connect_mysqldb(query)
