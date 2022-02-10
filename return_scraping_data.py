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
    sql = "SELECT place_name, race_number, one_3month_1win, one_6month_escape FROM all_race_data WHERE one_33month_1win >= 80 AND one_6month_escape >= 50;"
    cur.execute(sql)
    all_race_data = cur.fetchall()
    conn.commit()
    conn.close()
    print(all_race_data)
    return all_race_data


if __name__ == '__main__':
    return_scraping_data()
