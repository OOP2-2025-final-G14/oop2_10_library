# アプリ名: oop2_10_library

概要:
図書館アプリ
図書館利用者（ユーザー）の登録、本の登録、出版社の登録、本の貸し借りが行える。

## アピールポイント

本アプリは、図書館業務を想定した利用者管理・書籍管理・出版社管理・貸出管理を一元的に行えるWebアプリケーションである。

単に本に出版社名を文字列として持たせるのではなく、出版社を独立したデータとして管理し、本と結び付ける設計を採用している点が特徴である。
また、出版社の追加、書籍情報の増加、利用者数の増加といったケースにも柔軟に対応できる構造となっている。

<img width="1470" height="834" alt="Lapp01" src="https://github.com/user-attachments/assets/2e7dcc76-4d8d-4234-a5ff-144127de0008" />
<img width="1470" height="838" alt="Lapp03" src="https://github.com/user-attachments/assets/59977077-5d2d-4740-bf85-dbb03e83d055" />
<img width="1470" height="838" alt="Lapp05" src="https://github.com/user-attachments/assets/2fcd7f5c-11ed-4cd7-83eb-839c1a4633ae" />

図書館利用者（ユーザー）、本、出版社という複数のエンティティを整理し、それぞれを独立して管理することで、現実の図書館システムに近いデータ構造と処理の流れを実現している。

さらに、出版社別の貸出回数、利用者の年代別利用率、本ごとの貸出回数ランキングをグラフで一目見て理解することができる。

![library_app](https://github.com/user-attachments/assets/c283d912-065a-45c0-936f-a4aeb97a8f8e)

これにより、実際に図書館管理アプリとして運用する際、人気な本や利用者のボリューム層が一目で分かり、新しい本の仕入れの目安となる。


## 動作条件: require

```
python 3.13.7

# python lib
Flask==3.0.3
peewee==3.17.7
```

## 使い方: usage

```
$ python app.py
# Try accessing "http://localhost:8080" in your browser.
```
