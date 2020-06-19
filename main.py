#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run command ./main.py > test

# import MySQLdb
import pymysql
import argparse
import re

"""
პროგრამა ახდენს სიტყვების შემოწმებასა და მის ჩასწორებას
"""

server = "localhost"
user_name = "projectUser"
password = "projectUser!@3"
db_name = "Georgian_Words"
query = "select * from correct_words"
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
    data = cr.fetchall()
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
    correect_word_index = list()
    for index, alphabet in enumerate(data):
        incorrect_alphabet = 1
        alphabet_status = False
        word = alphabet["word_geo"]
        for input_index, input_word in enumerate(input_words_list):
            if (input_word == word):
                input_words_list[input_index] = word
                correect_word_index.append(input_index)
                print("==================================================correect words : {}".format(input_word))
                continue
            if input_index in correect_word_index:
                continue
            else:
                for i in range(len(input_word) - 1):
                    # print("")[1:5]
                    # ერთმანეთს დარდება ბაზაშI არსებული და პროგრამისთვის მინიჭებული სიტყვების ზომა
                    # თუ ბაზაშია რსბეული სიტყვის ზომა ნაკლებია მიწოდებულზე მაშინ  შემოწმებას აღარ გაივლის
                    if (word == input_word):
                        break
                    if ((len(word) < len(input_word)) or (len(word) > len(input_word) + 1)):
                        print("==========incorrect word")
                        break
                    # print(word, "44444444" + input_word)
                    # როდესაც სიტყვაში არსებული ასოები ერთმანეთს დაემთხვევა
                    if (input_word[i] == word[i]):
                        alphabet_status = True
                    # მოწმდება ინდექსი არის თუ არა სიტყვის ბოლო ასოზე
                    # კაცმა არ იცის აქ რახდება :D LMAO
                    elif (i != (len(input_word) - 1) and i != len(word) - 1):
                        print("range", i)
                        incorrect_alphabet += 1
                        if ((input_word[i] == word[i + 1]) and incorrect_alphabet <= 2):
                            # აქ ციკლის გაგრძელება არ უნდა მოხდეს რადგან შემდეგ ციკლზე ინდექსი გაიზრდება
                            # და შეტანილი სიტყვის ასოც შეიცვლება
                            index_for_word = i

                            for k in range(i, len(input_word) - i):
                                print("k=", k)
                                print("index = :", index_for_word)
                                if(k != len(word) - 1):
                                    ind = k + 1
                                    print("if-ind", ind)
                                    print("if-index", index_for_word)
                                    print("99999999999999", incorrect_alphabet)
                                if (input_word[index_for_word] != word[ind]):
                                    incorrect_alphabet += 1
                                    print("99999999999999", incorrect_alphabet)
                                index_for_word += 1

                            if(incorrect_alphabet <= 2):
                                input_words_list[input_index] = word
                                correect_word_index.append(input_index)
                                print("sworiii")

                            print("!!!!!!!!!!!!!!incorrect word  ")
                            break
                    else:
                        alphabet_status = False
                        incorrect_alphabet += 1
                        if((incorrect_alphabet == 1) and (i == len(input_word) - 1)):
                            input_words_list[input_index] = word
                        if(not alphabet_status):
                            if (input_word[1:len(input_word)] == word[1:len(input_word)]):
                                input_words_list[input_index] = word
    print(input_words_list)


if __name__ == "__main__":
    check_words(connect_and_fetch_data_db(query))
    generate_correct_sentence()
