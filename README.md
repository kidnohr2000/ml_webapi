# 機械学習結果の予測API

## 基本情報

### エンドポイント

|サービス|エンドポイント|Content-Type|備考|
|:--|:--|:--|:--|
|IRIS の予測API|/api/iris|application/json;UTF-8||
|ヘルスチェック|/api/sanity_check|application/json;UTF-8||

### ステータスコード

|ステータスコード|処理|
|:--|:--|
|400 (Bad Request)|バリデーションエラー|
|403 (Forbidden)|認可エラー|
|500 (Internal Server Error)|サーバ内部エラー|

## IF

### リクエスト

#### 基礎パラメータ

|param|カラム名|型|備考|
|:--|:--|:--|:--|
|callback|コールバック関数|文字列|上限20文字|

#### 変数用パラメータ

|param|カラム名|型|備考|
|:--|:--|:--|:--|
|sepal_length||数値|ガクの長さ(cm)|
|sepal_width||数値|ガクの幅(cm)|
|petal_length||数値|花弁の長さ(cm)|
|petal_width||数値|花弁の幅(cm)|

### レスポンス

### 基礎パラメータ

|param|カラム名|型|備考|
|:--|:--|:--|:--|
|meta|メタ情報|オブジェクト||
|meta.elapsed_time|レスポンスタイム|数値|マイクロ秒|
|meta.request_params|リクエストパラメータ|オブジェクト||
|results|予測結果|オブジェクト||
|results.label|ラベル|文字列||

#### results.label の値

|value|型|備考|
|:--|:--|:--|
|Setosa|文字列||
|Versicolor|文字列||
|Virginica|文字列||

## develop 環境

```shell
docker-compose -f docker-compose.dev.yml up --build
```

http://localhost:13081/api/iris?sepal_length=5.1&sepal_width=1&petal_length=1&petal_width=1
http://localhost:13081/api/sanity_check

## production 環境

```shell
docker-compose -f docker-compose.dev.yml up --build
docker-compose run api ./manage.py makemigrations api
docker-compose run api ./manage.py migrate
docker-compose -f docker-compose.dev.yml up
```

http://localhost:8000/api/iris?sepal_length=5.1&sepal_width=1&petal_length=1&petal_width=1
http://localhost:8000/api/sanity_check


## 環境

- Docker
- Nginx 1.17
- Posgresql latest
- Python3.6 (Django2.2, Django REST-framework)