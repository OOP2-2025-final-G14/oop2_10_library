from flask import Flask, render_template
from models import initialize_database, Publisher, Book
from peewee import *
from routes import blueprints

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    query = (Publisher
             .select(Publisher.name, fn.COUNT(Book.id).alias('book_count'))
             .join(Book)
             .group_by(Publisher)
             .order_by(fn.COUNT(Book.id).desc())
             .limit(5))

    # グラフ用にリスト化 (ラベルとデータ)
    labels = [p.name for p in query]
    data = [p.book_count for p in query]

    return render_template('index.html', labels=labels, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
