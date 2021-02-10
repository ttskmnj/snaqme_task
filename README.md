#  README
## requirements
- Docker
- Python 3.6以上
- pip

# 1. MySQL 設定
## MySQLコンテナ起動
```
$ docker run -d --name mysql-server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=passwd mysql
```

## データベース作成
```
$ mysql -h 0.0.0.0 -u root -e "CREATE DATABASE snaqme" -P 3306 -p
```

## sqlファイルからデータをインポート
```
$ mysql -h 0.0.0.0 -u root -D snaqme -p < db/sql_data.sql -P 3306
```
* 前もって `db` フォルダ以下に `sql_data.sql` をコピーしておく。

# 2. Flask設定 
* 以下の処理はレポジトリのルートフォルダで実行。
## 必要なライブラリのインストール
```
$ pip install requirements.txt 
```

## 環境変数 `FLASK_APP` を設定
```
$ export FLASK_APP=app.py
```

## Flask 起動
```
$ flask run
```

# 3. 動作確認
## 一覧
|URL|METHOD|
|---|------|
|http://127.0.0.1:5000/|GET|

### 返り値:
```
{
    result: [
        {
            calorie: "116",
            carb: "26",
            carbohydrate: "30.4",
            chara: "説明文が入ります-2 説明文が入ります-商品名-2 説明文が入ります-2 説明文が入ります-商品名-2 ",
            del_flg: 0,
            id: 2,
            images: "images-2",
            lipid: "0.2",
            loc_code: "A10",
            name: "商品名-2",
            protein: "1.6",
            regAt: 1456794806261,
            req_flg: 1,
            salt: null,
            status: 0,
            updAt: 1605616896000
        },
        ...
}
```

## 詳細
|URL|METHOD|
|---|------|
|http://127.0.0.1:5000/<ID>|GET|

### 返り値:
```
{
    
    name: "商品名-3",   
    chara: "説明文が入ります-3 説明文が入ります-商品名-3 説明文が入ります-3 説明文が入ります-商品名-3 ",
    id: 3,
    images: "images-3",
    status: 2,
    ingredients: [
        "タグ名-特徴-16",
        "タグ名-特徴-20",
        "タグ名-特徴-21",
        "タグ名-特徴-24",
        "タグ名-特徴-26",
        "タグ名-食感-32",
        "タグ名-味覚-207",
        "タグ名-味覚-211",
        "タグ名-同シリーズ-826",
        "タグ名-共通商品-688",
        "タグ名-成分-204",
        "タグ名-成分-1214"
    ],
    nutrition: {
        calorie: "27.1",
        carb: null,
        carbohydrate: null,
        lipid: null,
        protein: null,
        salt: null
    }
}
```

## 登録
|URL|METHOD|
|---|------|
|http://127.0.0.1:5000/|POST|

### POSTデータ
```
[('name', 'neimu'), ('status', '0'), ('images', 'imeiji'), ('chara', 'chara'), ('calorie', 'karori'), ('protein', 'purotein'), ('lipid', 'rippuid'), ('carbohydrate', 'ka-bonhaidoreito'), ('carb', 'ka-bu'), ('loc_code', 'locko-do'), ('req_flg', '0'), ('del_flg', '0'), ('salt', '1')]
```

### 返り値:
```
{
    "result": "created"
}
```

### データベース
```
mysql> select * from master_items ORDER BY id DESC LIMIT 1;
+------+-------+--------+--------+-------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| id   | name  | status | images | chara | calorie | protein  | lipid   | carbohydrate     | carb  | loc_code | req_flg | del_flg | regAt      | updAt      | salt |
+------+-------+--------+--------+-------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| 2079 | neimu |      0 | imeiji | chara | karori  | purotein | rippuid | ka-bonhaidoreito | ka-bu | locko-do |       0 |       0 | 1612966457 | 1612966457 |    1 |
+------+-------+--------+--------+-------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
1 row in set (0.00 sec)
```

## 更新
|URL|METHOD|
|---|------|
|http://127.0.0.1:5000/<ID>|PUT|

### PUTデータ
```
[('images', 'imeij put again 4'), ('chara', 'chara put again 3')]
```

### 返り値:
```
{
    "result": "updated"
}
```

### データベース
```mysql> select * from master_items where id = 2079;
+------+-------+--------+-------------------+-------------------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| id   | name  | status | images            | chara             | calorie | protein  | lipid   | carbohydrate     | carb  | loc_code | req_flg | del_flg | regAt      | updAt      | salt |
+------+-------+--------+-------------------+-------------------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| 2079 | neimu |      0 | imeij put again 4 | chara put again 3 | karori  | purotein | rippuid | ka-bonhaidoreito | ka-bu | locko-do |       0 |       0 | 1612966457 | 1612966457 |    1 |
+------+-------+--------+-------------------+-------------------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
1 row in set (0.00 sec)
```



## 削除
|URL|METHOD|
|---|------|
|http://127.0.0.1:5000/<ID>|DELETE|

### 返り値:
```
{
    "result": "deleted"
}
```

###  データベース
```
mysql> select * from master_items where id = 2079;
Empty set (0.01 sec)
```