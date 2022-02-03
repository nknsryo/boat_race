# noinspection PyUnresolvedReferences
import os

from dotenv import load_dotenv

load_dotenv()
import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


# webページを開くところまで。(driverは外に定義してある)
def web_open():
    driver.get(f"https://kyoteibiyori.com/race_shusso.php?place_no=1&race_no=1&hiduke=20220203&slider=1")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "wakubetsu2").click()

    driver.implicitly_wait(5)


# 1着率のリストを作る
def first():
    ittyaku = []

    ittyaku_ritsu = driver.find_element(By.XPATH,
                                        "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text

    time.sleep(3)

    ittyaku.append(ittyaku_ritsu)

    time.sleep(1)
    for count_up in range(6):
        first = driver.find_element(By.XPATH,
                                    f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[{count_up + 2}]").text
        ittyaku.append(first)

    print(ittyaku)

    time.sleep(1)


# 2着率のリストを作る
def second():
    ittyaku = []

    ittyaku_ritsu = driver.find_element(By.XPATH,
                                        "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text

    time.sleep(3)

    ittyaku.append(ittyaku_ritsu)

    time.sleep(1)
    for count_up in range(6):
        first = driver.find_element(By.XPATH,
                                    f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[{count_up + 2}]").text
        ittyaku.append(first)

    print(ittyaku)

    time.sleep(1)


# 決まり手
def third_kimarite():
    kimarite = []

    nige_ritsu = driver.find_element(By.XPATH,
                                     "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[26]/td").text

    time.sleep(3)

    kimarite.append(nige_ritsu)

    time.sleep(1)
    kimarite_1 = driver.find_element(By.XPATH,
                                     f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[29]/td[1]").text
    kimarite.append(kimarite_1)

    kimarite_2 = driver.find_element(By.XPATH,
                                     f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[40]/td[2]").text
    kimarite.append(kimarite_2)

    print(kimarite)


def main():
    web_open()
    # 1着率のリスト
    first()
    # 2着率のリスト
    second()
    # 決まり手
    third_kimarite()
    driver.close()


if __name__ == '__main__':
    main()
