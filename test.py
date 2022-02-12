# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
import datetime
# noinspection PyUnresolvedReferences
import chromedriver_binary
import schedule as schedule
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

from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.support.ui import WebDriverWait

from buy_ticket import buy_ticket_one_time

from datetime import date, timedelta


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options
    pass


# 定期購入>>>時間の15分前

# buy_today_tickets
# buy = 変数持ってくる
# 仮
buy = [('桐生', '12', '20:45', '2連単', 1, 4, 1, 10), ('戸田', '2', '11:19', '2連単', 1, 2, 1, 10),
       ('江戸川', '11', '15:47', '2連単', 1, 2, 1, 10).......]
for one_race_buy in range(0, len(buy)):

    入力を受け取る開催場名 = buy[one_race_buy][0]
    入力を受け取るレース番号 = buy[one_race_buy][1]
    入力を受け取るレース時間 = buy[one_race_buy][2] + datetime.timedelta(minutes=-15)
    入力を受け取る賭け式 = buy[one_race_buy][3]
    入力を受け取る1着の艇 = buy[one_race_buy][4]
    入力を受け取る2着の艇 = buy[one_race_buy][5]
    入力を受け取る掛け金額 = buy[one_race_buy][6]
    入金金額 = buy[one_race_buy][7]

    schedule.every().day.at(入力を受け取るレース時間).do(buy_ticket_one_time())
    while True:
        schedule.run_pending()
        sleep(1)

# 　時間で購入するメソッド　>>>>>buy_ticket_one_time()を回すためのもの


# 全レースの締切15分後に結果データを取得する
# 本日の払戻金一覧のページ
driver.get(f"https://www.boatrace.jp/owpc/pc/race/pay?hd={date()}")
time.sleep(3)
