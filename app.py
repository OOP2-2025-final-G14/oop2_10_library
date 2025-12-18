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
    publisher_query = (Publisher
        .select(Publisher.name, fn.COUNT(Borrow.id).alias('borrow_count'))
        .join(Book)  # 出版社 -> 本
        .join(Borrow)  # 本 -> 貸し出し
        .group_by(Publisher)
        .order_by(fn.COUNT(Borrow.id).desc())
        .limit(5))

    # 結果をリスト化（クエリ評価）
    publisher_results = list(publisher_query)

    # リスト内包表記で抽出（データがない場合は空リスト [] になる）
    publisher_labels = [p.name for p in publisher_results]
    publisher_data = [getattr(p, 'borrow_count', 0) for p in publisher_results]

    # 空の場合のデフォルト値をセット
    if not publisher_labels:
        publisher_labels = ["データなし"]
        publisher_data = [0]

    # ② 年代別 利用率（10代・20代…）
    age_expr = fn.FLOOR(User.age / 10) * 10

    age_query = (
        User
        .select(
            age_expr.alias('age_group'),
            fn.COUNT(Borrow.id).alias('cnt')
        )
        .join(Borrow)
        .group_by(age_expr)
    )

    age_labels = [f"{a.age_group}代" for a in age_query]
    age_values = [a.cnt for a in age_query]


    # ③ 本ごとの貸出回数
    book_query = (
        Book
        .select(Book.title, fn.COUNT(Borrow.id).alias('cnt'))
        .join(Borrow)
        .group_by(Book.title)
    )

    book_labels = [b.title for b in book_query]
    book_values = [b.cnt for b in book_query]

    return render_template(
        'index.html',
        publisher_labels=publisher_labels,
        publisher_values=publisher_data,
        age_labels=age_labels,
        age_values=age_values,
        book_labels=book_labels,
        book_values=book_values
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
