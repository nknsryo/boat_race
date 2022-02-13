# noinspection PyUnresolvedReferences
import os
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

import user_data
from user_data import all_user_data

load_dotenv()


# 全てのデーターを引っ張ってきて表示させる
def return_scraping_data():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # すべてのユーザー情報を取得

    # sql = "SELECT * FROM all_race_data WHERE place_name = 福岡";
    # cur.execute(sql)
    race = all_user_data()
    rate1 = race["user_rate1"]
    rate2 = race["user_rate2"]
    # print(rate1)
    # print(rate2)

    sql = "SELECT place_name, race_number, start_time ,two_3month_2win, three_3month_2win, four_3month_2win " \
          "FROM all_race_data " \
          f"WHERE one_3month_1win >= {rate1} AND one_6month_escape >= {rate2} " \
          "AND GREATEST(two_3month_2win, three_3month_2win, four_3month_2win) > GREATEST(five_3month_2win,six_3month_2win) " \
          "AND NOT two_3month_2win = three_3month_2win AND NOT two_3month_2win = four_3month_2win AND NOT three_3month_2win = four_3month_2win " \
          " ORDER BY start_time ASC;"
    cur.execute(sql)
    buy_race_data = cur.fetchall()
    conn.commit()
    conn.close()

    buy_tickets = []
    for i in range(0, len(buy_race_data)):
        place_name = buy_race_data[i][0]
        race_number = buy_race_data[i][1]
        start_time = buy_race_data[i][2]
        ticket_type = "2連単"
        first＿arrival = 1

        second＿arrival = 2
        if buy_race_data[i][3] < buy_race_data[i][4]:
            second＿arrival = 3
        elif buy_race_data[i][4] < buy_race_data[i][5]:
            second＿arrival = 4
        else:
            pass

        # race = all_user_data()
        race_place = race["user_race_place"]
        bet = race["user_bet"]
        deposit = race["user_deposit"]

        for x in race_place:
            if place_name == x:
                buy_tickets.append(
                    (place_name, race_number, start_time, ticket_type, first＿arrival, second＿arrival, bet, deposit))

    #     print(
    #         f"出走時間：{start_time} ｜ レース場：{place_name} ｜ レース番号： {race_number} ｜ チケットタイプ： {ticket_type} ｜ １着：{first＿arrival} ｜ ２着：{second＿arrival} ｜ 掛け金：{bet} ｜ 入金：{deposit}")
    # print(buy_tickets)
    return buy_tickets


if __name__ == '__main__':
    return_scraping_data()
