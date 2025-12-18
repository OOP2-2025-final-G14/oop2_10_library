from flask import Flask, render_template
from models import initialize_database, Publisher, Borrow, Book
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

    # --- 確認用 ---
    print(f"Labels: {labels}")
    print(f"Data: {data}")


    return render_template('index.html', labels=labels, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
