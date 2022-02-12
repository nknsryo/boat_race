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


driver = webdriver.Chrome(options=chromedriver_options())

# driver = webdriver.Chrome()
load_dotenv()

# 掛け方
入力を受け取る開催場名 = "蒲郡"
入力を受け取るレース番号 = 12
入力を受け取る賭け式 = "2連単"
入力を受け取る1着の艇 = 1
入力を受け取る2着の艇 = 3
入力を受け取る3着の艇 = 2
入力を受け取る掛け金額 = 1

place_list = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津", "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島",
              "宮島", "徳山", "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

# ログイン情報入力画面
handle_array = driver.window_handles
driver.switch_to.window(handle_array[0])

print(handle_array[0])

driver.get("https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/pc/race/pay%3FvoteTagId%3DcommonHead")
driver.implicitly_wait(5)
driver.find_element(By.NAME, "in_KanyusyaNo").send_keys(os.environ.get('USER_NUMBER_1'))
driver.find_element(By.NAME, "in_AnsyoNo").send_keys(os.environ.get('PASSWORD_1'))
driver.find_element(By.NAME, "in_PassWord").send_keys(os.environ.get('ATTESTATION_PASS_1'))
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/div/div[2]/div/form/p/button").click()

WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])

deposit = driver.find_element(By.XPATH, f"/html/body/div[1]/header/section[3]/div/p[2]/strong").text
print(deposit)

driver.close()
