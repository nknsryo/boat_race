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

    options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options
    pass


driver = webdriver.Chrome(options=chromedriver_options())

load_dotenv()


# driver = webdriver.Chrome()

def ticket():
    driver.get("https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/pc/race/pay%3FvoteTagId%3DcommonHead")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "in_KanyusyaNo").send_keys(os.environ.get('USER_NUMBER_1'))
    driver.find_element(By.NAME, "in_AnsyoNo").send_keys(os.environ.get('SECRET_NUMBER_1'))
    driver.find_element(By.NAME, "in_PassWord").send_keys(os.environ.get('PASSWORD_1'))
