#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run command ./main.py > test

# import MySQLdb
import pymysql
import argparse
import re

"""

მოსაფიქრებელია სიტყვების შედარებას როგორ მოვახდენთ.
როდესაც მიწოდებულ ტექსტიდან ამოვიღებთ სიტყვებს და ჩავსვავთ ლისტში შემდეგ
როგორ შევადგენთ წინადადებებს შესწორებული სიტყვებით
"""

server = "localhost"
user_name = "projectUser"
password = "projectUser!@3"
db_name = "Georgian_Words"
query = "select * from correct_words limit 50"
symbol_list = [",", ".", "?", "!", ":", ";", r'"']


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", type=str, help="teqsti romelic programam unda chaasworos", required=True)
args = parser.parse_args()
text = args.text
input_words_list = re.sub(r'[.!*"(),;:?]', ' ', text).split()
words_with_symbols = text.split()


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
    # print(type(data))
    # print(data)
    db.close()
    return data


def generate_correct_sentence():
    for index, word in enumerate(words_with_symbols):
        if(word[-1] in symbol_list):
            print(index, "boloshi" + word)
        if (word[0] in symbol_list):
            print("dasawyisshi")
            # length = len(input_words_list[index]) + 1


def check_words(data):
    for index, alphabet in enumerate(data):
        alphabet_status = False
        word = alphabet["word_geo"]
        for input_word in input_words_list:
            incorrect_alphabet = 0
            if (input_word == word):
                print("correect words : {}".format(input_word))
                continue
            else:
                for i in range(len(input_word) - 1):
                    # print("")[1:5]
                    # ერთმანეთს დარდება ბაზაშI არსებული და პროგრამისთვის მინიჭებული სიტყვების ზომა
                    # თუ ბაზაშია რსბეული სიტყვის ზომა ნაკლებია მიწოდებულზე მაშინ  შემოწმებას აღარ გაივლის
                    if (len(word) < len(input_word) - 1):
                        print("incorrect word")
                        print("==========")
                        break
                    # print(word, "44444444" + input_word)
                    # როდესაც სიტყვაში არსებული ასოები ერთმანეთს დაემთხვევა
                    if (input_word[i] == word[i]):
                        alphabet_status = True
                    # მოწმდება ინდექსი არის თუ არა სიტყვის ბოლო ასოზე
                    # კაცმა არ იცის აქ რახდება :D LMAO
                    elif (i != (len(input_word) - 1) and i != len(word) - 1):
                        print("range")
                        if ((input_word[i + 1] == word[i + 1]) and incorrect_alphabet <= 2):
                            print("gaagrdzelos cikli ")
                            continue
                            alphabet_status = True
                    else:
                        alphabet_status = False
                        incorrect_alphabet += 1
                    if(incorrect_alphabet == 1):
                        input_words_list[i] = word
                    if(not alphabet_status):
                        if (input_word[1:len(input_word)] == word[1:len(input_word)]):
                            input_words_list[i] = word

        # მიღებული გვაქვს სიტყვის თითოეული ასო
        # print(word)
        # print(words)


if __name__ == "__main__":
    check_words(connect_and_fetch_data_db(query))
    generate_correct_sentence()
