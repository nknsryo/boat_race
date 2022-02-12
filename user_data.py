# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import psycopg2 as psycopg2
# noinspection PyUnresolvedReferences
from dotenv import load_dotenv

load_dotenv()


# データベースの初期化
def init_db():
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続（コネクションを貼る）
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('schema_users.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる（）
    conn.close()


def create_user_data(user_data_lists):
    # >>>>>>>>データベースへ登録<<<<<<<<<
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続（コネクションを貼る）
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, user_data_lists)
    conn.commit()
    conn.close()


# 全てのデーターを引っ張ってきて表示させる

def all_user_data():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # すべてのユーザー情報を取得
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close()

    # ユーザーが選択したレース場情報
    user_race_place = users[0][0]
    user_race_place = user_race_place.replace("{", "")
    user_race_place = user_race_place.replace("}", "")
    user_race_place = user_race_place.split(',')
    # print(user_race_place)
    # ユーザーが入力したレート1情報
    user_rate1 = users[0][1]
    # print(user_rate1)
    # ユーザーが入力したレート2情報
    user_rate2 = users[0][2]
    # print(user_rate2)

    # ユーザーが入力した掛け金情報
    user_bet = users[0][3]
    # print(user_bet)

    # ユーザーが入力した入金情報
    user_deposit = users[0][4]
    # print(user_deposit)

    return {
        "user_race_place": user_race_place,
        "user_rate1": user_rate1,
        "user_rate2": user_rate2,
        "user_bet": user_bet,
        "user_deposit": user_deposit}
