# # # # # #
# # # # # # with open("test.csv", "a", encoding='utf_8_sig') as csv_file:
# # # # # #     {test.csv}
# # # # #
# # # # # with open("test.csv", "r", encoding="utf-8_sig") as f:
# # # # #     s = f.read()
# # # # # s = s.replace("'", "")
# # # # # s = s.replace("(", "")
# # # # # s = s.replace(")", "")
# # # # #
# # # # #
# # # # # with open("test.csv", "w", encoding="utf-8_sig") as f:
# # # # #     f.write(s)
# # # # # noinspection PyUnresolvedReferences
# # # # import os
# # # #
# # # # import time
# # # # import datetime
# # # # # noinspection PyUnresolvedReferences
# # # # import chromedriver_binary
# # # # from selenium import webdriver
# # # # # noinspection PyUnresolvedReferences
# # # # from selenium.webdriver.common.by import By
# # # # # noinspection PyUnresolvedReferences
# # # # from selenium.webdriver.common.keys import Keys
# # # # # noinspection PyUnresolvedReferences
# # # # import csv
# # # #
# # # #
# # # # def date():
# # # #     dt_now = datetime.datetime.now()
# # # #     year = dt_now.year
# # # #     month = str(dt_now.month).zfill(2)
# # # #     day = str(dt_now.day).zfill(2)
# # # #     today_date = f"{year}{month}{day}"
# # # #     return today_date
# # # #     pass
# # # #
# # # #
# # # # def chromedriver_options():
# # # #     # オプション設定
# # # #     options = webdriver.ChromeOptions()
# # # #
# # # #     options.add_argument('--headless')
# # # #     options.add_argument("--window-size=1280,1280")
# # # #     return options
# # # #     pass
# # # #
# # # #
# # # # driver = webdriver.Chrome(options=chromedriver_options())
# # # #
# # # # # driver = webdriver.Chrome()
# # # # # driver.get("https://kyoteibiyori.com/race_shusso.php?place_no=1&race_no=2&hiduke=20220208&slider=1")
# # # # # time.sleep(2)
# # # # # # test_text = driver.find_element(By.XPATH, F"/html/body/div[8]/div[1]/section/div[3]/h2").text
# # # # # # test_text = test_text.split("締切")[1]
# # # # # # test_text = test_text.split("お気")[0]
# # # # # # print(test_text)
# # # # # # driver.close()
# # # # # for player_name in range(1, 7):
# # # # #     players_name = driver.find_element(By.XPATH,
# # # # #                                        f"/html/body/div[8]/div[1]/section/div[3]/div[2]/table/tbody/"
# # # # #                                        f"tr[3]/td[{player_name}]").text
# # # # #     players_name_1 = players_name.split("\n")[0]
# # # # #     players_name_2 = players_name.split("\n")[1]
# # # # #     players_name = f"{players_name_1} {players_name_2}"
# # # # #
# # # # #     print(players_name)
# # # # #
# # # # # driver.close()
# # # #
# # # #
# # # #
# # # # with open("test.csv", 'r+') as f:
# # # #     f.truncate(0)
# # # #
# import os
#
# import psycopg2 as psycopg2
# from dotenv import load_dotenv
#
# from db import init_db, add_data
#
# load_dotenv()
# # #
# # # init_db()
# # #
# # # # data,place_name,race_number,first_text,one_3month_1win,two_3month_1win,three_3month_1win,four_3month_1win,five_3month_1win,six_3month_1win,second_text,oen_3month_2win,two_3month_2win,three_3month_2win,four_3month_2win,five_3month_2win,six_3month_2win,third_text,one_3month_3win,two_3month_3win,three_3month_3win,four_3month_3win,five_3month_3win,six_3month_3win,kimarite_text,one_6month_escape,one_6month_escaped,
# #
# #
# # {'date':= race_info[0},{'place_name_scra':= race_info[1},{'race_numb':= race_info[2},{'first_te':= race_info[3},{'one_3month_1w':= race_info[4},{'two_3month_1w':= race_info[5},{'three_3month_1w':= race_info[6},{'four_3month_1w':= race_info[7},{'five_3month_1w':= race_info[8},{'six_3month_1w':= race_info[9},{'second_text': race_info[10},{'oen_3month_2win': race_info[11},{'two_3month_2win': race_info[12},{'three_3month_2win': race_info[13},{'four_3month_2win': race_info[14},{'five_3month_2win': race_info[15},{'six_3month_2win': race_info[16},{'third_text': race_info[17},{'one_3month_3win': race_info[18},{'two_3month_3win': race_info[19},{'three_3month_3win': race_info[20},{'four_3month_3win': race_info[21},{'five_3month_3win': race_info[22},{'six_3month_3win': race_info[23},{'kimarite_text': race_info[24},{'one_6month_escape': race_info[25},{'one_6month_escaped': race_info[26},
# #
# #
# #
# #
#

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

load_dotenv()

# def init_db():
#     # Connectionを貼る
#     dsn = os.environ.get('DATABASE_URL')
#     connection = psycopg2.connect(dsn)
#
#     # カーソルオブジェクトを作る
#     cursor = connection.cursor()
#     with open('schema.sql', encoding='utf-8') as f:
#         cursor.execute(f.read())
#
#     # 変更内容を保存する
#     connection.commit()
#
#     # コネクションを閉じる
#     connection.close()
#
#
# def register_user(name, age):
#     # Connectionを貼る
#     dsn = os.environ.get('DATABASE_URL')
#     connection = psycopg2.connect(dsn)
#
#     cursor = connection.cursor()
#
#     sql = f"INSERT INTO all_race_data (data,place_number) VALUES ('{name}', {age})"
#
#     cursor.execute(sql)
#
#     connection.commit()
#
#     connection.close()
#
#
# def main():
#     init_db()
#     name = 'Bob'
#     age = 19
#     sex = 'man'
#
#
#     register_user(name, age)
#
# if __name__ == "__main__":
#     main()


import sqlite3

dsn = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(dsn)
cursor = connection.cursor()

# テーブルを作成
cursor.execute('schema.sql', encoding='utf-8')

# レコードを登録
keys = ['data', 'place_name', 'race_number', 'name_1', 'name_2', 'name_3', 'name_4', 'name_5', 'name_6', 'first_text',
        'one_3month_1win', 'two_3month_1win', 'three_3month_1win', 'four_3month_1win', 'five_3month_1win',
        'six_3month_1win', 'second_text', 'oen_3month_2win', 'two_3month_2win', 'three_3month_2win', 'four_3month_2win',
        'five_3month_2win', 'six_3month_2win', 'third_text', 'one_3month_3win', 'two_3month_3win', 'three_3month_3win',
        'four_3month_3win', 'five_3month_3win', 'six_3month_3win', 'kimarite_text', 'one_6month_escape',
        'one_6month_escaped']
values = race_info
new_data = dict(zip(keys, values))
new_data
cursor.executemany("INSERT INTO all_race_data VALUES (?, ?)", new_data)

cursor.execute('select * from all_race_data')
docs = cursor.fetchall()
for doc in docs:
        print(doc)

connection.commit()

connection.close()
