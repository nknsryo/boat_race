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


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # ヘッドレスモード
    # return options


def main():
    chromedriver_options()

    data_place = []
    # data_placeはlistだよ！

    # driver = webdriver.Chrome(options=chromedriver_options())
    driver = webdriver.Chrome()

    driver.get("https://kyoteibiyori.com/race_shusso.php?place_no=1&race_no=1&hiduke=20220203&slider=1")

    driver.implicitly_wait(10)

    driver.find_element(By.ID, "wakubetsu2").click()

    driver.implicitly_wait(5)

    one = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text

    time.sleep(3)

    data_place.append(one)

    time.sleep(1)

    a = driver.find_element(By.XPATH,
                            "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[2]").text
    data_place.append(a)

    b = driver.find_element(By.XPATH,
                            "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[3]").text
    data_place.append(b)

    c = driver.find_element(By.XPATH,
                            "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[4]").text
    data_place.append(c)

    d = driver.find_element(By.XPATH,
                            "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[5]").text
    data_place.append(d)

    e = driver.find_element(By.XPATH,
                            "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[6]").text
    data_place.append(e)

    f = driver.find_element(By.XPATH,
                            "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[7]").text
    data_place.append(f)
    # 48~70 forでまとめる

    time.sleep(1)

    print(data_place)

    driver.close()


if __name__ == '__main__':
    main()
