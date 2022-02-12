-- もしテーブルが存在したら削除
DROP TABlE IF EXISTS users;

-- もしテーブルがなかったら作成  customers--テーブル名
CREATE TABLE IF NOT EXISTS users(
    user_race_place TEXT,
    user_rate1 INTEGER,
    user_rate2 INTEGER,
    user_bet INTEGER,
    user_deposit INTEGER
);
