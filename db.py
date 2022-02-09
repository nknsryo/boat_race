import csv
import os

import psycopg2 as psycopg2
from dotenv import load_dotenv

# from all_data_db import race_info

load_dotenv()


def init_db():
    # Connectionを貼る
    dsn = os.environ.get('DATABASE_URL')
    connection = psycopg2.connect(dsn)

    cursor = connection.cursor()

    with open('schema.sql', encoding='utf-8') as f:
        cursor.execute(f.read())

    connection.commit()

    connection.close()


# def scraping_data_all():
#     data = race_info[0]
#     place_name_scrape = race_info[1]
#     race_number = race_info[2]
#     first_text = race_info[3]
#     one_3month_1win = race_info[4]
#     two_3month_1win = race_info[5]
#     three_3month_1win = race_info[6]
#     four_3month_1win = race_info[7]
#     five_3month_1win = race_info[8]
#     six_3month_1win = race_info[9]
#     second_text = race_info[10]
#     oen_3month_2win = race_info[11]
#     two_3month_2win = race_info[12]
#     three_3month_2win = race_info[13]
#     four_3month_2win = race_info[14]
#     five_3month_2win = race_info[15]
#     six_3month_2win = race_info[16]
#     third_text = race_info[17]
#     one_3month_3win = race_info[18]
#     two_3month_3win = race_info[19]
#     three_3month_3win = race_info[20]
#     four_3month_3win = race_info[21]
#     five_3month_3win = race_info[22]
#     six_3month_3win = race_info[23]
#     kimarite_text = race_info[24]
#     one_6month_escape = race_info[25]
#     one_6month_escaped = race_info[26]


def add_user_column(data, place_name, race_number, name_1, name_2, name_3, name_4, name_5, name_6, first_text,
                    one_3month_1win,
                    two_3month_1win, three_3month_1win, four_3month_1win, five_3month_1win, six_3month_1win,
                    second_text,
                    oen_3month_2win, two_3month_2win, three_3month_2win, four_3month_2win, five_3month_2win,
                    six_3month_2win,
                    third_text, one_3month_3win, two_3month_3win, three_3month_3win, four_3month_3win, five_3month_3win,
                    six_3month_3win, kimarite_text, one_6month_escape, one_6month_escaped):
    # Connectionを貼る
    dsn = os.environ.get('DATABASE_URL')
    connection = psycopg2.connect(dsn)

    cursor = connection.cursor()

    sql = f"INSERT INTO users (data,place_name_scrape,race_number," \
          f"name_1,name_2,name_3,name_4,name_5,name_6," \
          f"first_text,one_3month_1win,two_3month_1win,three_3month_1win,four_3month_1win,five_3month_1win,six_3month_1win," \
          f"second_text,oen_3month_2win,two_3month_2win,three_3month_2win,four_3month_2win,five_3month_2win,six_3month_2win," \
          f"third_text,one_3month_3win,two_3month_3win,three_3month_3win,four_3month_3win,five_3month_3win,six_3month_3win," \
          f"kimarite_text,one_6month_escape,one_6month_escaped) " \
          f"VALUES ({race_info[0]},{race_info[1]},{race_info[2]}," \
          f"{race_info[3]},{race_info[4]},{race_info[5]},{race_info[6]},{race_info[7]},{race_info[8]}," \
          f"{race_info[9]},{race_info[10]},{race_info[11]},{race_info[12]},{race_info[13]},{race_info[14]}," \
          f"{race_info[15]},{race_info[16]},{race_info[17]},{race_info[18]},{race_info[19]},{race_info[20]}," \
          f"{race_info[21]},{race_info[22]},{race_info[23]},{race_info[24]},{race_info[25]},{race_info[25]}," \
          f"{race_info[27]},{race_info[28]},{race_info[29]},{race_info[30]},{race_info[31]},{race_info[32]})"

    cursor.execute(sql)

    connection.commit()

    connection.close()

#
init_db()
# scraping_data_all()
# add_user()
# def scraping_data():
#     data = race_info[0]
#     place_name = race_info[1]
#     race_number = race_info[2]
#     first_text = race_info[3]
#     one_3month_1win = race_info[4]
#     two_3month_1win = race_info[5]
#     three_3month_1win = race_info[6]
#     four_3month_1win = race_info[7]
#     five_3month_1win = race_info[8]
#     six_3month_1win = race_info[9]
#     second_text = race_info[10]
#     oen_3month_2win = race_info[11]
#     two_3month_2win = race_info[12]
#     three_3month_2win = race_info[13]
#     four_3month_2win = race_info[14]
#     five_3month_2win = race_info[15]
#     six_3month_2win = race_info[16]
#     third_text = race_info[17]
#     one_3month_3win = race_info[18]
#     two_3month_3win = race_info[19]
#     three_3month_3win = race_info[20]
#     four_3month_3win = race_info[21]
#     five_3month_3win = race_info[22]
#     six_3month_3win = race_info[23]
#     kimarite_text = race_info[24]
#     one_6month_escape = race_info[25]
#     one_6month_escaped = race_info[26]
