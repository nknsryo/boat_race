# from datetime import *
# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
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

from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.support.ui import WebDriverWait
from return_scraping_data import return_scraping_data

import datetime


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options
    pass


def now_time():
    dt_now = datetime.datetime.now()
    hour = str(dt_now.hour).zfill(2)
    minutes = str(dt_now.minute).zfill(2)
    now_date = f"{hour}{minutes}00"
    return now_date
    pass


def buy_ticket_one_time():
    # driver = webdriver.Chrome(options=chromedriver_options())
    driver = webdriver.Chrome()
    load_dotenv()

    for one_race_buy_1 in range(0, len(buy_tickets)):

        入力を受け取るレース時間 = datetime.datetime.combine(datetime.datetime.now(),
                                                 buy_tickets[one_race_buy_1][2]) - datetime.timedelta(minutes=15)
        入力を受け取るレース時間 = f"{入力を受け取るレース時間}"
        入力を受け取るレース時間 = 入力を受け取るレース時間.split(" ")
        入力を受け取るレース時間 = 入力を受け取るレース時間[1]
        入力を受け取るレース時間 = datetime.datetime.strptime(入力を受け取るレース時間, "%H:%M:%S").time()

        入力を受け取る開催場名 = buy_tickets[one_race_buy_1][0]
        入力を受け取るレース番号 = buy_tickets[one_race_buy_1][1]
        入力を受け取る賭け式 = buy_tickets[one_race_buy_1][3]
        入力を受け取る1着の艇 = buy_tickets[one_race_buy_1][4]
        入力を受け取る2着の艇 = buy_tickets[one_race_buy_1][5]
        入力を受け取る掛け金額 = buy_tickets[one_race_buy_1][6]
        入金金額 = buy_tickets[one_race_buy_1][7]
        if int((f"{入力を受け取るレース時間}").replace(":", "")) < int(now_time()):
            continue
        # print(入力を受け取るレース時間)
        # ログイン情報入力画面
        driver.get("https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/pc/race/pay%3FvoteTagId%3DcommonHead")
        driver.implicitly_wait(5)
        # 個人情報を入力
        driver.find_element(By.NAME, "in_KanyusyaNo").send_keys(os.environ.get('USER_NUMBER_1'))
        driver.find_element(By.NAME, "in_AnsyoNo").send_keys(os.environ.get('PASSWORD_1'))
        driver.find_element(By.NAME, "in_PassWord").send_keys(os.environ.get('ATTESTATION_PASS_1'))
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/div/div[2]/div/form/p/button").click()
        driver.implicitly_wait(5)

        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])

        # 入金メソッド
        # デポジット額取得
        deposit = driver.find_element(By.XPATH, f"/html/body/div[1]/header/section[3]/div/p[2]/strong").text
        deposit = deposit.replace(",", "")
        time.sleep(6)
        if int(1000) >= int(deposit) < 入力を受け取る掛け金額 * 100:
            # 少なければ追加入金z
            driver.find_element(By.XPATH, "/html/body/div[1]/header/section[1]/div/nav/ul/li[1]/a/span").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "/html/body/div[1]/header/section[1]/div/nav/ul/li[1]/ul/li[1]").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, f"/html/body/div[1]/header/div[1]/div/div[2]/div[1]/span[2]/input").send_keys(
                str(入金金額))
            driver.find_element(By.XPATH, f"/html/body/div[1]/header/div[1]/div/div[2]/div[2]/span[2]/input").send_keys(
                os.environ.get('VOTE_PASS_1'))
            time.sleep(2)
            driver.find_element(By.XPATH, f"/html/body/div[1]/header/div[1]/div/ul/li[1]/a").click()
            time.sleep(5)
            driver.find_element(By.XPATH, f"/html/body/div[7]/div/ul/li[1]/a").click()
            time.sleep(2)
            driver.find_element(By.XPATH, f"/html/body/div[1]/header/div[1]/div/ul/li/a").click()
            time.sleep(2)
        else:
            pass

        # 入金画面操作ここまで

        place_list = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津", "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀",
                      "児島",
                      "宮島", "徳山", "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

        for place_number in range(1, 25):
            if place_list[place_number - 1] == f"{入力を受け取る開催場名}":  #
                driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[3]/ul/li[{place_number}]").click()
                driver.implicitly_wait(5)
            else:
                pass
        time.sleep(2)

        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[1]/section[2]/ul/li[{入力を受け取るレース番号}]").click()

        time.sleep(2)

        bet_theory_list = ["3連単", "3連複", "2連単", "2連複", "拡連複"]
        for bet_theory in range(1, 6):
            if bet_theory_list[bet_theory - 1] == f"{入力を受け取る賭け式}":  #
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[1]/ul/li[{bet_theory}]").click()
            else:
                pass

        # 通常投票をクリック
        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[2]/ul/li[1]").click()

        time.sleep(2)
        boat_rank_list = [1, 2, 3, 4, 5, 6]
        if f"{入力を受け取る賭け式}" == "3連単" or f"{入力を受け取る賭け式}" == "3連複":
            for boat_rank1 in range(1, 7):
                if boat_rank_list[boat_rank1 - 1] == int(f"{入力を受け取る1着の艇}"):  #
                    driver.find_element(By.XPATH,
                                        f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{boat_rank1 + 1}]/td[8]").click()
                    time.sleep(1)
                else:
                    continue
            for boat_rank2 in range(1, 7):
                if boat_rank_list[boat_rank2 - 1] == int(f"{入力を受け取る2着の艇}"):  #
                    driver.find_element(By.XPATH,
                                        f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{boat_rank2 + 1}]/td[9]").click()
                    time.sleep(1)
                else:
                    continue
            for boat_rank3 in range(1, 7):
                if boat_rank_list[boat_rank3 - 1] == int(f"{入力を受け取る3着の艇}"):  #
                    driver.find_element(By.XPATH,
                                        f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{boat_rank3 + 1}]/td[10]").click()
                    time.sleep(1)
                else:
                    continue
        elif f"{入力を受け取る賭け式}" == "2連単" or f"{入力を受け取る賭け式}" == "2連複" or f"{入力を受け取る賭け式}" == "拡連複":
            for boat_rank1 in range(1, 7):
                if boat_rank_list[boat_rank1 - 1] == int(f"{入力を受け取る1着の艇}"):  #
                    driver.find_element(By.XPATH,
                                        f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{boat_rank1 + 1}]/td[8]").click()
                    time.sleep(1)
                else:
                    continue
            for boat_rank2 in range(1, 7):
                if boat_rank_list[boat_rank2 - 1] == int(f"{入力を受け取る2着の艇}"):  #
                    driver.find_element(By.XPATH,
                                        f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{boat_rank2 + 1}]/td[9]").click()
                    time.sleep(1)
                else:
                    continue
        else:
            pass

        time.sleep(2)
        # 購入金額の入力
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[4]/div[1]/input").send_keys(
            int(f"{入力を受け取る掛け金額}"))
        time.sleep(2)
        # ベットリストに追加ボタンをクリック
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[4]/div[2]").click()
        time.sleep(2)
        # 投票入力完了ボタンをクリック
        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[5]/section/div[3]/div[3]").click()

        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/section[4]/div[2]/form/p[1]/input").send_keys(
            int(f"{入力を受け取る掛け金額}") * 100)
        time.sleep(2)

        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/section[4]/div[2]/form/p[2]/input").send_keys(
            os.environ.get('VOTE_PASS_1'))
        time.sleep(2)

        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/section[4]/div[2]/form/div[2]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, f"/html/body/div[7]/div/ul/li[1]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, f"/html/body/div[1]/header/section[1]/div/ul/li[3]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, f"/html/body/div[7]/div/ul/li[1]/a").click()
        time.sleep(2)

        handle_array = driver.window_handles
        driver.switch_to.window(handle_array[0])

    driver.close()


#
# driver = webdriver.Chrome(options=chromedriver_options())
#
# load_dotenv()
#
#
# driver = webdriver.Chrome()


# for one_race_buy_1 in range(0, len(buy_tickets)):
#
#     入力を受け取る開催場名 = buy_tickets[one_race_buy_1][0]
#     入力を受け取るレース番号 = buy_tickets[one_race_buy_1][1]
#     入力を受け取るレース時間 = buy_tickets[one_race_buy_1][2] - datetime.timedelta(minutes=15)
#
#     入力を受け取る賭け式 = buy_tickets[one_race_buy_1][3]
#     入力を受け取る1着の艇 = buy_tickets[one_race_buy_1][4]
#     入力を受け取る2着の艇 = buy_tickets[one_race_buy_1][5]
#     入力を受け取る掛け金額 = buy_tickets[one_race_buy_1][6]
#     入金金額 = buy_tickets[one_race_buy_1][7]
#     print(入力を受け取るレース時間)
#     schedule.every().day.at(入力を受け取るレース時間).do(buy_ticket_one_time())
#     while True:
#         schedule.run_pending()
#         sleep(1)
#

buy_tickets = return_scraping_data()
buy_ticket_one_time()
