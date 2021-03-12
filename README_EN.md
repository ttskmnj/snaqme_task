#  README in English
## Requirements
- Docker
- Python 3.6 
- pip

# 1. Set up MySQL
## Set MySQL password to environment variable
```
$ export DB_PASSWD=<password>
```

## Run MySQL container
```
$ docker run -d --name mysql-server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$DB_PASSWD mysql
```

## Creat Database
```
$ mysql -h 0.0.0.0 -u root -e "CREATE DATABASE snaqme" -P 3306 --password=$DB_PASSWD
Enter password: 
```

## Import data from SQL file
Creat `db` directory under repository root and put `sql_data.sql` in it.

```
$ mysql -h 0.0.0.0 -u root -D snaqme --password=$DB_PASSWD < db/sql_data.sql -P 3306
```

# 2. Set up Flask 
## Install required libraries
```
$ pip install -r requirements.txt 
```

## Set environment varible `FLASK_APP` 
```
$ export FLASK_APP=app.py
```

## run Flask
```
$ flask run
```

# 3. API Document
## List
|URL|METHOD|
|---|------|
|http\://127.0.0.1:5000/|GET|

#### Return:
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

## Detail
|URL|METHOD|
|---|------|
|http\://127.0.0.1:5000/\<ID\>|GET|

#### Return:
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

## Register
|URL|METHOD|
|---|------|
|http\://127.0.0.1:5000/|POST|

#### POST Data
```
[('name', 'neimu'), ('status', '0'), ('images', 'imeiji'), ('chara', 'chara'), ('calorie', 'karori'), ('protein', 'purotein'), ('lipid', 'rippuid'), ('carbohydrate', 'ka-bonhaidoreito'), ('carb', 'ka-bu'), ('loc_code', 'locko-do'), ('req_flg', '0'), ('del_flg', '0'), ('salt', '1')]
```

#### Return:
```
{
    "result": "created"
}
```

#### Database result
```
mysql> select * from master_items ORDER BY id DESC LIMIT 1;
+------+-------+--------+--------+-------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| id   | name  | status | images | chara | calorie | protein  | lipid   | carbohydrate     | carb  | loc_code | req_flg | del_flg | regAt      | updAt      | salt |
+------+-------+--------+--------+-------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| 2079 | neimu |      0 | imeiji | chara | karori  | purotein | rippuid | ka-bonhaidoreito | ka-bu | locko-do |       0 |       0 | 1612966457 | 1612966457 |    1 |
+------+-------+--------+--------+-------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
1 row in set (0.00 sec)
```

## Update
|URL|METHOD|
|---|------|
|http\://127.0.0.1:5000/\<ID\>|PUT|

#### PUT data
```
[('images', 'imeij put again 4'), ('chara', 'chara put again 3')]
```

#### Return:
```
{
    "result": "updated"
}
```

#### Database result
```mysql> select * from master_items where id = 2079;
+------+-------+--------+-------------------+-------------------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| id   | name  | status | images            | chara             | calorie | protein  | lipid   | carbohydrate     | carb  | loc_code | req_flg | del_flg | regAt      | updAt      | salt |
+------+-------+--------+-------------------+-------------------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
| 2079 | neimu |      0 | imeij put again 4 | chara put again 3 | karori  | purotein | rippuid | ka-bonhaidoreito | ka-bu | locko-do |       0 |       0 | 1612966457 | 1612966457 |    1 |
+------+-------+--------+-------------------+-------------------+---------+----------+---------+------------------+-------+----------+---------+---------+------------+------------+------+
1 row in set (0.00 sec)
```



## Delete
|URL|METHOD|
|---|------|
|http\://127.0.0.1:5000/\<ID\>|DELETE|

#### Return:
```
{
    "result": "deleted"
}
```

####  Database result
```
mysql> select * from master_items where id = 2079;
Empty set (0.01 sec)
```