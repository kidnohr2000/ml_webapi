# IRIS の予測API

## IF

### リクエスト

### 基礎パラメータ

||||

### 変数用パラメータ

|param|カラム名|型|備考|
|:--|:--|:--|:--|
|sepal_length||数値|ガクの長さ(cm)|
|sepal_width||数値|ガクの幅(cm)|
|petal_length||数値|花弁の長さ(cm)|
|petal_width||数値|花弁の幅(cm)|

## label

|value|型|備考|
|:--|:--|:--|
|Setosa|文字列||
|Versicolor|文字列||
|Virginica|文字列||

## develop 環境

docker-compose -f docker-compose.dev.yml up --build

http://localhost:13081/api/iris?sepal_length=5.1&sepal_width=1&petal_length=1&petal_width=1


## production 環境

http://localhost:8000/api/iris?sepal_length=5.1&sepal_width=1&petal_length=1&petal_width=1