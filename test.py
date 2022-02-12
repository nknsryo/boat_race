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


# この時間の15分まえのリストを作らないといけない。
# 定期購入
# buy_today_tickets

start_times = ["11:15", "13:52", "19:22"]  # リストから呼び出す。
for buy_time in start_times:
    schedule.every().day.at(f"{buy_time}").do(buy_ticket_one_time())
