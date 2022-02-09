

-- もしテーブルが存在したら削除
DROP TABlE IF EXISTS all_race_data;

-- もしテーブルがなかったら作成  customers--テーブル名
CREATE TABLE IF NOT EXISTS all_race_data(
    date_ TEXT,
    place_name TEXT,
    start_time TEXT,
    race_number TEXT,
    name_1 TEXT,
    name_2 TEXT,
    name_3 TEXT,
    name_4 TEXT,
    name_5 TEXT,
    name_6 TEXT,
    first_text TEXT,
    one_3month_1win INTEGER,
    two_3month_1win INTEGER,
    three_3month_1win INTEGER,
    four_3month_1win INTEGER,
    five_3month_1win INTEGER,
    six_3month_1win INTEGER,
    second_text TEXT,
    one_3month_2win INTEGER,
    two_3month_2win INTEGER,
    three_3month_2win INTEGER,
    four_3month_2win INTEGER,
    five_3month_2win INTEGER,
    six_3month_2win INTEGER,
    third_text TEXT,
    one_3month_3win INTEGER,
    two_3month_3win INTEGER,
    three_3month_3win INTEGER,
    four_3month_3win INTEGER,
    five_3month_3win INTEGER,
    six_3month_3win INTEGER,
    kimarite_text TEXT,
    one_6month_escape INTEGER,
    two_6month_escaped INTEGER

)
--
--  テストデータの挿入
--INSERT INTO
--    -- customers(name, age)とかにするとカラム指定ができる。
--    customers
--VALUES
--    ('Bob', 15),
--    ('Tom', 57),
--    ('Ken', 76)
--    ;