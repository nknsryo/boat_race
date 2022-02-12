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

load_dotenv()


# 全てのデーターを引っ張ってきて表示させる
def return_scraping_data():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # すべてのユーザー情報を取得

    # sql = "SELECT * FROM all_race_data WHERE place_name = 福岡";
    # cur.execute(sql)

    sql = "SELECT place_name, race_number, start_time ,two_3month_2win, three_3month_2win, four_3month_2win " \
          "FROM all_race_data " \
          "WHERE one_3month_1win >= 80 AND one_6month_escape >= 50 " \
          "AND GREATEST(two_3month_2win, three_3month_2win, four_3month_2win) > GREATEST(five_3month_2win,six_3month_2win) " \
          "AND NOT two_3month_2win = three_3month_2win AND NOT two_3month_2win = four_3month_2win AND NOT three_3month_2win = four_3month_2win;"
    cur.execute(sql)
    buy_race_data = cur.fetchall()
    conn.commit()
    conn.close()

    buy = []
    for i in range(0, len(buy_race_data)):
        place_name = buy_race_data[i][0]
        race_number = buy_race_data[i][1]
        ticket_type = "2連単"
        first＿arrival = 1

        second＿arrival = 2
        if buy_race_data[i][3] < buy_race_data[i][4]:
            second＿arrival = 3
        elif buy_race_data[i][4] < buy_race_data[i][5]:
            second＿arrival = 4
        else:
            pass

        bet = 1
        choice_place = ["鳴門", "福岡"]

        for x in choice_place:
            if place_name == x:
                buy.append((place_name, race_number, ticket_type, first＿arrival, second＿arrival, bet))
            else:
                pass
        print(
            f"レース場：{place_name} ｜ レース番号： {race_number} ｜ チケットタイプ： {ticket_type} ｜ １着：{first＿arrival} ｜ ２着：{second＿arrival} ｜ 掛け金：{bet}")
    print(buy)
    return buy_race_data


if __name__ == '__main__':
    return_scraping_data()
