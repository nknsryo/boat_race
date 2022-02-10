# noinspection PyUnresolvedReferences
import os

import time
import datetime
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys
# noinspection PyUnresolvedReferences
import csv

# noinspection PyUnresolvedReferences
import psycopg2 as psycopg2
# noinspection PyUnresolvedReferences
from dotenv import load_dotenv

from db import init_db

load_dotenv()
init_db()

dsn = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(dsn)

cursor = connection.cursor()

with open('test.csv', newline='') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        sql = "INSERT INTO all_race_data VALUES('{}','{}','')"
        sql = sql.format(str(row[0]), row[1])
        cursor.execute(sql)
        connection.commit()

cursor.close()
connection.close()

# with open('test.csv') as fp:
#     cursor.copy_from(fp, table='  a    ', sep=',',
#                      columns=['date', 'place_name’,’start_time’,’race_number', 'name_1', 'name_2', 'name_3', 'name_4',
#                               'name_5', 'name_6', 'first_text', 'one_3month_1win', 'two_3month_1win',
#                               'three_3month_1win', 'four_3month_1win', 'five_3month_1win', 'six_3month_1win',
#                               'second_text', 'oen_3month_2win', 'two_3month_2win', 'three_3month_2win',
#                               'four_3month_2win', 'five_3month_2win', 'six_3month_2win', 'third_text',
#                               'one_3month_3win', 'two_3month_3win', 'three_3month_3win', 'four_3month_3win',
#                               'five_3month_3win', 'six_3month_3win', 'kimarite_text', 'one_6month_escape',
#                               'one_6month_escaped'])
# connection.commit()
#
# #
#
# def add_data_01():
#     dsn = os.environ.get('DATABASE_URL')
#     connection = psycopg2.connect(dsn)
#
#     cursor = connection.cursor()
#
#     sql = '''
#     insert into users (
#        data,
#        place_name,
#        start_time,
#        race_number,
#        name_1,
#        name_2,
#        name_3,
#        name_4,
#        name_5,
#        name_6,
#        first_text,
#        one_3month_1win,
#        two_3month_1win,
#        three_3month_1win,
#        four_3month_1win,
#        five_3month_1win,
#        six_3month_1win,
#        second_text,
#        oen_3month_2win,
#        two_3month_2win,
#        three_3month_2win,
#        four_3month_2win,
#        five_3month_2win,
#        six_3month_2win,
#        third_text,
#        one_3month_3win,
#        two_3month_3win,
#        three_3month_3win,
#        four_3month_3win,
#        five_3month_3win,
#        six_3month_3win,
#        kimarite_text,
#        one_6month_escape,
#        one_6month_escaped'
#        VALUE(
#        %(race_info[0])s
#        %(race_info[1])s
#        %(race_info[2])s
#        %(race_info[3])s
#        %(race_info[4])s
#        %(race_info[5])s
#        %(race_info[6])s
#        %(race_info[7])s
#        %(race_info[8])s
#        %(race_info[9])s
#        %(race_info[10])s
#        %(race_info[11])s
#        %(race_info[12])s
#        %(race_info[13])s
#        %(race_info[14])s
#        %(race_info[15])s
#        %(race_info[16])s
#        %(race_info[17])s
#        %(race_info[18])s
#        %(race_info[19])s
#        %(race_info[20])s
#        %(race_info[21])s
#        %(race_info[22])s
#        %(race_info[23])s
#        %(race_info[24])s
#        %(race_info[25])s
#        %(race_info[25])s
#        %(race_info[27])s
#        %(race_info[28])s
#        %(race_info[29])s
#        %(race_info[30])s
#        %(race_info[31])s
#        %(race_info[32])s
#        %(race_info[33])s
#         )
#         '''
#     # address = ['東京都渋谷区恵比寿', '東京都渋谷区恵比寿西', '東京都渋谷区恵比寿南']
#     # column_name =['data','place_name','start_time','race_number','name_1','name_2','name_3','name_4','name_5','name_6','first_text','one_3month_1win','two_3month_1win','three_3month_1win','four_3month_1win','five_3month_1win','six_3month_1win','second_text','oen_3month_2win','two_3month_2win','three_3month_2win','four_3month_2win','five_3month_2win','six_3month_2win','third_text','one_3month_3win','two_3month_3win','three_3month_3win','four_3month_3win','five_3month_3win','six_3month_3win','kimarite_text','one_6month_escape','one_6month_escaped']
#     # race_info
#     # # リストを辞書へ統合
#     # adr_dict = dict(zip(column_name, race_info))
#     options ={'data':race_info[0],'place_name':race_info[1],'start_time': race_info[2],'race_number':race_info[3],'name_1':race_info[4],'name_2':race_info[5],'name_3':race_info[6],'name_4':race_info[7],'name_5':race_info[8],'name_6':race_info[9],'first_text':race_info[10],'one_3month_1win':race_info[11],'two_3month_1win':race_info[12],'three_3month_1win':race_info[13],'four_3month_1win':race_info[14],'five_3month_1win':race_info[15],'six_3month_1win':race_info[16],'second_text':race_info[17],'oen_3month_2win':race_info[18],'two_3month_2win':race_info[19],'three_3month_2win':race_info[20],'four_3month_2win':race_info[21],'five_3month_2win':race_info[22],'six_3month_2win':race_info[23],'third_text':race_info[24],'one_3month_3win':race_info[25],'two_3month_3win':race_info[26],'three_3month_3win':race_info[27],'four_3month_3win':race_info[28],'five_3month_3win':race_info[29],'six_3month_3win':race_info[30],'kimarite_text':race_info[31],'one_6month_escape':race_info[32],'one_6month_escaped':race_info[33]}
#     cursor.execute(sql, options)
#     connection.commit()
#     connection.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


import psycopg2

dsn = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(dsn)
cursor = connection.cursor()
with open('test.csv') as fp:
    cursor.copy_from(fp, table='all_race_data', sep=',',
                     columns=['data', 'place_name’,’start_time’,’race_number', 'name_1', 'name_2', 'name_3', 'name_4',
                              'name_5', 'name_6', 'first_text', 'one_3month_1win', 'two_3month_1win',
                              'three_3month_1win', 'four_3month_1win', 'five_3month_1win', 'six_3month_1win',
                              'second_text', 'oen_3month_2win', 'two_3month_2win', 'three_3month_2win',
                              'four_3month_2win', 'five_3month_2win', 'six_3month_2win', 'third_text',
                              'one_3month_3win', 'two_3month_3win', 'three_3month_3win', 'four_3month_3win',
                              'five_3month_3win', 'six_3month_3win', 'kimarite_text', 'one_6month_escape',
                              'one_6month_escaped'])
connection.commit()

# dbにいれる
# dsn = os.environ.get('DATABASE_URL')
# connection = psycopg2.connect(dsn)
#
# cursor = connection.cursor()
#
# sql = '''
# insert into users (
#    data,
#    place_name,
#    start_time,
#    race_number,
#    name_1,
#    name_2,
#    name_3,
#    name_4,
#    name_5,
#    name_6,
#    first_text,
#    one_3month_1win,
#    two_3month_1win,
#    three_3month_1win,
#    four_3month_1win,
#    five_3month_1win,
#    six_3month_1win,
#    second_text,
#    oen_3month_2win,
#    two_3month_2win,
#    three_3month_2win,
#    four_3month_2win,
#    five_3month_2win,
#    six_3month_2win,
#    third_text,
#    one_3month_3win,
#    two_3month_3win,
#    three_3month_3win,
#    four_3month_3win,
#    five_3month_3win,
#    six_3month_3win,
#    kimarite_text,
#    one_6month_escape,
#    one_6month_escaped'
#    VALUE(
#    %(race_info[0])s
#    %(race_info[1])s
#    %(race_info[2])s
#    %(race_info[3])s
#    %(race_info[4])s
#    %(race_info[5])s
#    %(race_info[6])s
#    %(race_info[7])s
#    %(race_info[8])s
#    %(race_info[9])s
#    %(race_info[10])s
#    %(race_info[11])s
#    %(race_info[12])s
#    %(race_info[13])s
#    %(race_info[14])s
#    %(race_info[15])s
#    %(race_info[16])s
#    %(race_info[17])s
#    %(race_info[18])s
#    %(race_info[19])s
#    %(race_info[20])s
#    %(race_info[21])s
#    %(race_info[22])s
#    %(race_info[23])s
#    %(race_info[24])s
#    %(race_info[25])s
#    %(race_info[25])s
#    %(race_info[27])s
#    %(race_info[28])s
#    %(race_info[29])s
#    %(race_info[30])s
#    %(race_info[31])s
#    %(race_info[32])s
#    %(race_info[33])s
#     )
#     '''
# # address = ['東京都渋谷区恵比寿', '東京都渋谷区恵比寿西', '東京都渋谷区恵比寿南']
# # column_name =['data','place_name','start_time','race_number','name_1','name_2','name_3','name_4','name_5','name_6','first_text','one_3month_1win','two_3month_1win','three_3month_1win','four_3month_1win','five_3month_1win','six_3month_1win','second_text','oen_3month_2win','two_3month_2win','three_3month_2win','four_3month_2win','five_3month_2win','six_3month_2win','third_text','one_3month_3win','two_3month_3win','three_3month_3win','four_3month_3win','five_3month_3win','six_3month_3win','kimarite_text','one_6month_escape','one_6month_escaped']
# # race_info
# # # リストを辞書へ統合
# # adr_dict = dict(zip(column_name, race_info))
# options = {'data': race_info[0], 'place_name': race_info[1], 'start_time': race_info[2],
#            'race_number': race_info[3], 'name_1': race_info[4], 'name_2': race_info[5],
#            'name_3': race_info[6], 'name_4': race_info[7], 'name_5': race_info[8], 'name_6': race_info[9],
#            'first_text': race_info[10], 'one_3month_1win': race_info[11], 'two_3month_1win': race_info[12],
#            'three_3month_1win': race_info[13], 'four_3month_1win': race_info[14],
#            'five_3month_1win': race_info[15], 'six_3month_1win': race_info[16],
#            'second_text': race_info[17], 'oen_3month_2win': race_info[18], 'two_3month_2win': race_info[19],
#            'three_3month_2win': race_info[20], 'four_3month_2win': race_info[21],
#            'five_3month_2win': race_info[22], 'six_3month_2win': race_info[23], 'third_text': race_info[24],
#            'one_3month_3win': race_info[25], 'two_3month_3win': race_info[26],
#            'three_3month_3win': race_info[27], 'four_3month_3win': race_info[28],
#            'five_3month_3win': race_info[29], 'six_3month_3win': race_info[30],
#            'kimarite_text': race_info[31], 'one_6month_escape': race_info[32],
#            'one_6month_escaped': race_info[33]}
# cursor.execute(sql, options)
# connection.commit()
# connection.close()
#
# # dbここまで
