from flask import Flask, render_template
from models import initialize_database, Publisher, Borrow, Book
from peewee import *
from routes import blueprints
from models import Borrow, Book, Publisher, User
from peewee import fn
import json

app = Flask(__name__)


initialize_database()


for blueprint in blueprints:
    app.register_blueprint(blueprint)


@app.route('/')
def index():
    query = (Publisher
        .select(Publisher.name, fn.COUNT(Borrow.id).alias('borrow_count'))
        .join(Book)  # 出版社 -> 本
        .join(Borrow)  # 本 -> 貸し出し
        .group_by(Publisher)
        .order_by(fn.COUNT(Borrow.id).desc())
        .limit(5))

    # グラフ用にリスト化 (ラベルとデータ)
    labels = [p.name for p in query]
    data = [p.borrow_count for p in query]
    # 結果をリスト化（クエリ評価）
    results = list(query)

    # リスト内包表記で抽出（データがない場合は空リスト [] になる）
    labels = [p.name for p in results]
    data = [getattr(p, 'borrow_count', 0) for p in results]

    # 空の場合のデフォルト値をセット
    if not labels:
        labels = ["データなし"]
        data = [0]


    return render_template(
        'index.html',
        publisher_labels=publisher_labels,
        publisher_values=publisher_values,
        age_labels=age_labels,
        age_values=age_values,
        book_labels=book_labels,
        book_values=book_values
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
