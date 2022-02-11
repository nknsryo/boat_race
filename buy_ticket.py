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


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options
    pass


#
# driver = webdriver.Chrome(options=chromedriver_options())
#
# load_dotenv()
#
#
# driver = webdriver.Chrome()

def buy_ticket_one_time():
    driver = webdriver.Chrome(options=chromedriver_options())
    # driver = webdriver.Chrome()
    load_dotenv()

    # 掛け方
    入力を受け取る開催場名 = "鳴門"
    入力を受け取るレース番号 = 6
    入力を受け取る賭け式 = "2連単"
    入力を受け取る1着の艇 = 1
    入力を受け取る2着の艇 = 3
    入力を受け取る3着の艇 = 2
    入力を受け取る掛け金 = 100

    # ログイン情報入力画面
    driver.get("https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/pc/race/pay%3FvoteTagId%3DcommonHead")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "in_KanyusyaNo").send_keys(os.environ.get('USER_NUMBER_1'))
    time.sleep(1)
    driver.find_element(By.NAME, "in_AnsyoNo").send_keys(os.environ.get('PASSWORD_1'))
    time.sleep(1)
    driver.find_element(By.NAME, "in_PassWord").send_keys(os.environ.get('ATTESTATION_PASS_1'))
    time.sleep(1)
    
    # 古いウィンドウのWindowハンドル取得
    wh_before = driver.window_handles

    driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/div/div[2]/div/form/p/button").click()
    driver.implicitly_wait(20)

    time.sleep(1)
    # 新規Windowを開いたあとのWindowハンドル一覧を取得
    wh_after = driver.window_handles
    # Windowハンドル一覧の比較を行い、新規で開いたWindowのハンドルを取得
    new_window = set(wh_after).difference(set(wh_before)).pop()
    # 新規Windowに切り替え
    driver.switch_to.window(new_window)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/p/a").click()
    driver.implicitly_wait(30)

    place_list = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津", "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島",
                  "宮島", "徳山", "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

    for place_number in range(1, 25):
        if place_list[place_number - 1] == f"{入力を受け取る開催場名}":  #
            return place_number
        else:
            pass
        driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[3]/ul/li[{place_number}]").click()

    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[1]/section[2]/ul/li[{入力を受け取るレース番号}]").click()

    bet_theory_list = ["3連単", "3連複", "2連単", "2連複", "拡連複"]
    for bet_theory in range(1, 6):
        if bet_theory_list[bet_theory - 1] == f"{入力を受け取る賭け式}":  #
            return bet_theory
        else:
            pass
        # 賭け式を選択
        driver.find_element(By.XPATH,
                            f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[1]/ul/li[{bet_theory}]").click()
    # 通常投票をクリック
    driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[2]/ul/li[1]").click()

    if f"{入力を受け取る賭け式}" == "3連単" or f"{入力を受け取る賭け式}" == "3連複":
        # 1着の艇をクリック
        for choose_no1 in range(1, 7):
            if choose_no1 == f"{int(入力を受け取る1着の艇)}":  #
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{choose_no1 + 1}]/td[8]").click()
            else:
                pass
        # 2着の艇をクリック
        for choose_no1 in range(1, 7):
            if choose_no1 == f"{int(入力を受け取る2着の艇)}":
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{choose_no1 + 1}]/td[9]").click()
            else:
                pass
        # 3着の艇をクリック
        for choose_no1 in range(1, 7):
            if choose_no1 == f"{int(入力を受け取る3着の艇)}":
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{choose_no1 + 1}]/td[10]").click()
            else:
                pass

    elif f"{入力を受け取る賭け式}" == "2連単" or f"{入力を受け取る賭け式}" == "2連複" or f"{入力を受け取る賭け式}" == "拡連複":
        # 1着の艇をクリック
        for choose_no1 in range(1, 7):
            if choose_no1 == "int({入力を受け取る(1着の艇)})":
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{choose_no1 + 1}]/td[8]").click()
            else:
                pass
        # 2着の艇をクリック
        for choose_no1 in range(1, 7):
            if choose_no1 == "int({入力を受け取る(2着の艇)})":
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[1]/table/tbody/tr[{choose_no1 + 1}]/td[9]").click()
    else:
        pass
    # 購入金額の入力
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[4]/div[1]/input").send_keys(
        int(f"{入力を受け取る掛け金}") / 100)
    # 別途リストに追加ボタンをクリック
    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section/div[2]/div[3]/div[4]/div[2]").click()
    # 投票入力完了ボタンをクリック
    driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[5]/section/div[3]/div[3]").click()

    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/section[4]/div[2]/form/p[1]/input").send_keys(
        f"{入力を受け取る掛け金}")
    driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/section[4]/div[2]/form/p[2]/input").send_keys(
        os.environ.get('VOTE_PASS_1'))
    driver.find_element(By.XPATH, f"/html/body/div[1]/main/div/section[4]/div[2]/form/div[2]/a").click
    driver.find_element(By.XPATH, f"/html/body/div[7]/div/ul/li[1]/a").click
    driver.find_element(By.XPATH, f"/html/body/div[1]/header/section[1]/div/ul/li[3]/a").click()
    driver.find_element(By.XPATH, f"/html/body/div[7]/div/ul/li[1]/a").click()

    driver.close()


buy_ticket_one_time()
