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


# def chromedriver_options():
#     # オプション設定
#     options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')  # ヘッドレスモード
#     return options


def main():
    # chromedriver_options()
    # driver = webdriver.Chrome(options=chromedriver_options())
    driver = webdriver.Chrome()
    for place_number in range(1, 25):
        race_info = []
        driver.get("https://kyoteibiyori.com/")
        race_place_text = driver.find_element(By.XPATH,
                                              f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{place_number}]").text
        x = "出走なし"
        if x in race_place_text:
            pass
            # continue
        else:
            place_name = driver.find_element(By.XPATH, f"/html/body/div[4]/div/section[1]/div[2]/ul/"
                                                       f"li[{place_number}]/a/div[1]").text
            place_name_button = driver.find_element(By.XPATH, f"/html/body/div[4]/div/section[1]/div[2]/ul/"
                                                              f"li[{place_number}]/a/div[1]")
            race_info.append(place_name)
            place_name_button.click()
            driver.implicitly_wait(4)
            driver.find_element(By.XPATH,
                                "/html/body/div[5]/div[1]/section/div[3]/div[2]/table/tbody/tr[1]/td[2]").click()
            driver.implicitly_wait(4)
            for race_number in range(1, 13):
                driver.find_element(By.ID, "wakubetsu2").click()
                driver.implicitly_wait(1)
                first_win_rate = driver.find_element(By.XPATH, f"").text
                driver.find_element(By.XPATH, f"").text
                driver.find_element(By.XPATH, f"").text
                driver.find_element(By.XPATH, f"").text
                driver.find_element(By.XPATH, f"").text

                driver.implicitly_wait(5)

                # レース番号
                race_number = driver.find_element(By.XPATH,
                                                  "/html/body/div[8]/div[1]/section/div[2]/table/tbody/tr[1]/td[1]").text

                # 1着率のリスト
                ittyaku = []

                ittyaku_ritsu = driver.find_element(By.XPATH,
                                                    "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text

                time.sleep(3)
                ittyaku.append(race_number)
                ittyaku.append(ittyaku_ritsu)

                time.sleep(1)
                for count_up in range(6):
                    first = driver.find_element(By.XPATH,
                                                f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[{count_up + 2}]").text
                    ittyaku.append(first)

                print(ittyaku)

                time.sleep(1)

                # 2着率のリスト
                nittyaku = []

                nittyaku_ritsu = driver.find_element(By.XPATH,
                                                     "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[6]/td").text

                time.sleep(3)

                nittyaku.append(nittyaku_ritsu)

                time.sleep(1)
                for count_up_2 in range(6):
                    second = driver.find_element(By.XPATH,
                                                 f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[9]/td[{count_up_2 + 2}]").text
                    nittyaku.append(second)

                print(nittyaku)

                # 決まり手
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

                one_race_data = []
                one_race_data.append(ittyaku)
                one_race_data.append(nittyaku)
                one_race_data.append(kimarite)
                print(list(one_race_data))

                driver.close()


if __name__ == '__main__':
    main()
