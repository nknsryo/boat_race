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


def main():
    driver.get("https://kyoteibiyori.com/")
    for hold_place_number in range(24):
        # 1番目の開催場(桐生)のアイコン
        hold_place = driver.find_element(By.XPATH,
                                         f"/html/body/div[3]/div/section[1]/div[2]/ul/li[{hold_place_number}+1]")

        hold_place_text = driver.find_element(By.XPATH,
                                              f"/html/body/div[3]/div/section[1]/div[2]/ul/li[{hold_place_number}+1]").text
        # 1番目の開催場の名前をテキスト化する
        x = "出走なし"

        if x in hold_place_text:
            pass
        else:
            hold_place.click()
            # 1R目の枠別勝率をクリック
            driver.find_element(By.XPATH,
                                f"/html/body/div[5]/div[1]/section/div[3]/div[2]/table/tbody/tr[1]/td[2]/a").click()
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "wakubetsu2").click()
            driver.implicitly_wait(5)

            race_list = []
        for number in range(12):
            race_number = number + 1

            race_list.append(hold_place_text)
            race_list.append(race_number)

            # 1着率のリスト

            first_place = driver.find_element(By.XPATH,
                                              "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text
            race_list.append(first_place)

        for count_up_1 in range(6):
            first_place_player_each = driver.find_element(By.XPATH,
                                                          f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[{count_up_1 + 2}]").text
            race_list.append(first_place_player_each)

            time.sleep(1)

            # 2着率のリスト

            second_place = driver.find_element(By.XPATH,
                                               "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[6]/td").text
            race_list.append(second_place)

            time.sleep(1)

        for count_up_2 in range(6):
            second_place_player_each = driver.find_element(By.XPATH,
                                                           f"/html/body/div[8]/div[1]/section/"
                                                           f"div[5]/table[1]/tbody/tr[9]/td"
                                                           f"[{count_up_2 + 2}]").text
            race_list.append(second_place_player_each)

            time.sleep(1)

            run_away_probability = driver.find_element(By.XPATH,
                                                       "/html/body/div[8]/div[1]/section/"
                                                       "div[5]/table[1]/tbody/tr[26]/"
                                                       "td").text
            race_list.append(run_away_probability)
            time.sleep(1)
            kimarite_1 = driver.find_element(By.XPATH,
                                             f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[29]/td[1]").text
            race_list.append(kimarite_1)

            kimarite_2 = driver.find_element(By.XPATH,
                                             f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[40]/td[2]").text
            race_list.append(kimarite_2)

        print(race_list)

    driver.close()


if __name__ == '__main__':
    main()
