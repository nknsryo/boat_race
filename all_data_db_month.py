# noinspection PyUnresolvedReferences
import os
import time
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

import calendar

load_dotenv()


def csv_method(race_info):
    with open("test_02.csv", 'r+') as f:
        f.truncate(0)
    with open("test_02.csv", "a", encoding='utf_8_sig') as csv_file:
        print(race_info, file=csv_file)
    with open("test_02.csv", "r", encoding="utf-8_sig") as f:
        s = f.read()
    s = s.replace("'", "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("[", "")
    s = s.replace("]", "")
    # csv(累計レース)書き込み
    with open("test_02.csv", "w", encoding="utf-8_sig") as f:
        f.write(s)
    # csvファイルの加工(",","()","[]")削除、更新
    with open("test.csv", "r", encoding="utf-8_sig") as f:
        s = f.read()
    s = s.replace("'", "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("[", "")
    s = s.replace("]", "")
    with open("test.csv", "w", encoding="utf-8_sig") as f:
        f.write(s)
    with open("test.csv", "a", encoding='utf_8_sig') as csv_file:
        print(race_info, file=csv_file)
    # print(race_info)


# noinspection PyUnresolvedReferences


def date():
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = str(dt_now.month).zfill(2)
    day = str(dt_now.day).zfill(2)
    today_date = f"{year}{month}{day}"
    return today_date
    pass


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options
    pass


def scraping_register_data():
    load_dotenv()
    driver = webdriver.Chrome(options=chromedriver_options())

    # driver = webdriver.Chrome()

    # test.csvのフォルダ内を空にする
    with open("test.csv", 'r+') as f:
        f.truncate(0)

    init_db()

    race_year = 2022
    # 1年間のデータ取得
    for race_month in range(1, 3):
        days = calendar.monthrange(race_year, race_month)[1]
        # 24レース場からデータを取得してくる
        for race_day in range(1, days + 1):
            if len(str(race_month)) == 1:
                race_month = f"0{race_month}"
            if len(str(race_day)) == 1:
                race_day = f"0{race_day}"
            chose_race_date = f"{race_year}{race_month}{race_day}"
            # driver.get(f"https://kyoteibiyori.com/index.php?hiduke={chose_race_date}")
            for race_place in range(1, 25):
                time.sleep(3)
                # ボートレース日和の当日のトップページを表示
                driver.get(f"https://kyoteibiyori.com/index.php?hiduke={chose_race_date}")
                driver.implicitly_wait(20)
                x = "中止"
                y = "出走なし"
                # 開催場名をテキスト情報として取得
                race_place_text = driver.find_element(By.XPATH,
                                                      f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{race_place}]").text
                # "中止"という文字が入っているかどうか
                stop_race = x in race_place_text
                # "出走なし"という文字が入っているかどうか
                none_race = y in race_place_text
                if stop_race:
                    # "中止"という文字が入っていたら処理をとばす
                    continue
                elif none_race:
                    # "出走なし"という文字が入っていたら処理をとばす
                    continue
                else:
                    # それ以外の条件の時に情報を取得できるようにする
                    place_name = driver.find_element(By.XPATH,
                                                     f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{race_place}]/a/div[1]").text
                    # 1~12レースの情報を回す。
                for race_number in range(1, 13):
                    # それぞれの開催場の枠別情報のページを表示
                    driver.get(f"https://kyoteibiyori.com/race_shusso.php?"
                               f"place_no={race_place}&race_no={race_number}&hiduke={chose_race_date}&slider=1")
                    time.sleep(2)
                    driver.implicitly_wait(5)
                    # 一般戦のボタンをクリック
                    driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/section/div[5]/div[1]/div/ul/li[2]").click()
                    driver.implicitly_wait(3)
                    race_info = []
                    # スタート時間を取得
                    start_time = driver.find_element(By.XPATH, F"/html/body/div[8]/div[1]/section/div[3]/h2").text
                    start_time = start_time.split("締切")[1]
                    start_time = start_time.split(" ")[0]
                    start_time = start_time.split("\n")[0]
                    start_time = datetime.datetime.strptime(start_time, '%H:%M').time()
                    # リストに　日付　を追加
                    day = chose_race_date
                    # day = datetime.datetime.strptime(day, '%Y%m%d').chose_race_date
                    race_info.append(day)
                    # race_info.append(chose_race_date)
                    # リストに　開催場　を追加
                    race_info.append(place_name)
                    # リストに　出走時間　を追加
                    race_info.append(start_time)
                    # "1着率"という文字情報を取得
                    first_win_rate = driver.find_element(By.XPATH,
                                                         "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text
                    # リストに　レース番号　を追加
                    race_info.append(f"{race_number}")
                    # リストに選手名を追加
                    for player_name in range(1, 7):
                        players_name = driver.find_element(By.XPATH,
                                                           f"/html/body/div[8]/div[1]/section/div[3]/div[2]/table/tbody/"
                                                           f"tr[3]/td[{player_name}]").text
                        if "\n" in players_name:
                            players_name_1 = players_name.split("\n")[0]
                            players_name_2 = players_name.split("\n")[1]
                            players_name = f"{players_name_1} {players_name_2}"
                        else:
                            players_name = players_name
                        race_info.append(players_name)

                    # リストに　"1着率"　という文字を追加
                    race_info.append(F"3ヶ月{first_win_rate}")
                    # 1~6号艇の1着率を取ってくる
                    for first_win_rate_player in range(1, 7):

                        three_month_1win = driver.find_element(By.XPATH,
                                                               f"/html/body/div[8]/div[1]/section/div[5]"
                                                               f"/table[1]/tbody/tr[4]/td[{first_win_rate_player + 1}]").text
                        # 情報が"-"の時は"0"として表示する
                        if three_month_1win == "-":
                            three_month_1win = "0.0%1"
                        else:
                            pass
                        # %より前に記載してある数字の部分のみを表示してリストに追加
                        three_month_1win = three_month_1win.split("%")[0]
                        three_month_1win = int(three_month_1win.split(".")[0])
                        race_info.append(three_month_1win)
                    driver.implicitly_wait(2)

                    second_in_rate = driver.find_element(By.XPATH,
                                                         f"/html/body/div[8]/div[1]/section/div[5]"
                                                         f"/table[1]/tbody/tr[6]/td").text
                    race_info.append(second_in_rate)
                    # 1~6号艇の2連対率
                    for second_in_rate_player in range(1, 7):
                        three_month_2win = driver.find_element(By.XPATH,
                                                               f"/html/body/div[8]/div[1]/section/div[5]"
                                                               f"/table[1]/tbody/tr[9]/td[{second_in_rate_player + 1}]").text
                        # 情報が"-"の時は"0"として表示する
                        if three_month_2win == "-":
                            three_month_2win = "0.0%1"
                        else:
                            pass
                        # %より前に記載してある数字の部分のみを表示してリストに追加
                        three_month_2win = three_month_2win.split("%")[0]
                        three_month_2win = int(three_month_2win.split(".")[0])
                        race_info.append(three_month_2win)

                    third_in_rate = driver.find_element(By.XPATH,
                                                        f"/html/body/div[8]/div[1]/section/div[5]/"
                                                        f"table[1]/tbody/tr[11]/td").text
                    race_info.append(third_in_rate)
                    for third_in_rate_player in range(1, 7):
                        three_month_3win = driver.find_element(By.XPATH,
                                                               f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/"
                                                               f"tr[14]/td[{third_in_rate_player + 1}]").text
                        # 情報が"-"の時は"0"として表示する
                        if three_month_3win == "-":
                            three_month_3win = "0.0%1"
                        else:
                            pass
                        # %より前に記載してある数字の部分のみを表示してリストに追加
                        three_month_3win = three_month_3win.split("%")[0]
                        three_month_3win = int(three_month_3win.split(".")[0])
                        race_info.append(three_month_3win)

                    # "逃げ率"というテキスト情報を取得、追加
                    determination_way = driver.find_element(By.XPATH,
                                                            f"/html/body/div[8]/div[1]/section/div[5]"
                                                            f"/table[1]/tbody/tr[26]/td").text
                    race_info.append(determination_way)
                    # 逃げ率　を取得、リストに追加していく
                    escape_rate = driver.find_element(By.XPATH, f"/html/body/div[8]/div[1]/section/div[5]"
                                                                f"/table[1]/tbody/tr[29]/td[1]").text
                    # 逃し率　を取得、リストに追加していく
                    escaped_rate = driver.find_element(By.XPATH, f"/html/body/div[8]/div[1]/section/div[5]"
                                                                 f"/table[1]/tbody/tr[29]/td[2]").text

                    if escape_rate == "-":
                        escape_rate = "0.0%1"
                    if escaped_rate == "-":
                        escaped_rate = "0.0%1"
                    escape_rate = escape_rate.split("%")[0]
                    escape_rate = int(escape_rate.split(".")[0])

                    escaped_rate = escaped_rate.split("%")[0]
                    escaped_rate = int(escaped_rate.split(".")[0])
                    race_info.append(escape_rate)
                    race_info.append(escaped_rate)
                    driver.implicitly_wait(5)
                    # test.csvに書き込み
                    csv_method(race_info)
                    # race_info = tuple(race_info)
                    print(race_info)

                    # >>>>>>>>データベースへ登録<<<<<<<<<
                    # DBの情報を取得
                    dsn = os.environ.get('DATABASE_URL')
                    # DBに接続（コネクションを貼る）
                    conn = psycopg2.connect(dsn)
                    cur = conn.cursor()

                    sql = "INSERT INTO all_race_data VALUES (" \
                          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                          "%s, %s, %s, %s)"
                    cur.execute(sql, race_info)
                    conn.commit()
                    conn.close

    driver.close()


# データベースの初期化
def init_db():
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続（コネクションを貼る）
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる（）
    conn.close()


def main():
    init_db()
    scraping_register_data()


if __name__ == "__main__":
    main()
