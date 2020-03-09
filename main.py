#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run command ./main.py > test


import MySQLdb

server = "localhost"
user_name = "projectUser"
password = "projectUser!@3"
db_name = "Georgian_Words"
query = "select * from correct_words"


def connect_mysqldb(query):
    try:
        db = MySQLdb.connect(server, user_name, password, db_name, charset='utf8')
        print(db)
    except Exception as ex:
        print(ex)

    cr = db.cursor(MySQLdb.cursors.DictCursor)
    cr.execute(query)
    data = cr.fetchone()
    print(type(data))
    print(data["Word"])
    return data


if __name__ == "__main__":
    connect_mysqldb(query)
