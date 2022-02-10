-- もしテーブルが存在したら削除
DROP TABlE IF EXISTS users;

-- もしテーブルがなかったら作成  customers--テーブル名
CREATE TABLE IF NOT EXISTS users(
    kiryu INTEGER,
    toda INTEGER,
    edogawa INTEGER,
    tamagawa INTEGER,
    heiwajima INTEGER,
    hamanako INTEGER,
    gamagoori INTEGER,
    tokoname INTEGER,
    tsu INTEGER,
    mikuni INTEGER,
    biwako INTEGER,
    suminoe INTEGER,
    amagasaki INTEGER,
    naruto INTEGER,
    marugame INTEGER,
    kojima INTEGER,
    miyajima INTEGER,
    tokuyama INTEGER,
    shimonoseki INTEGER,
    wakamatsu INTEGER,
    ashiya INTEGER,
    hukuoka INTEGER,
    karatsu INTEGER,
    oomura INTEGER
)
