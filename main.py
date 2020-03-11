#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run command ./main.py > test

# import MySQLdb
import pymysql
import argparse


server = "localhost"
user_name = "projectUser"
password = "projectUser!@3"
db_name = "Georgian_Words"
query = "select * from correct_words limit 50 "

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", type=str, help="teqsti romelic programam unda chaasworos", required=True)
args = parser.parse_args()
text = args.text
print(text)


def connect_and_fetch_data_db(query):
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
    return data


def check_words(data):
    for alphabet in data:
        words = alphabet["word_geo"]
        for word in words:
            # მიღებული გვაქვს სიტყვის თითოეული ასო
            print(word)


if __name__ == "__main__":
    check_words(connect_and_fetch_data_db(query))
