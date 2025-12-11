from flask import Blueprint, render_template, request, redirect, url_for
from models import Publisher

# Blueprintの作成
publisher_bp = Blueprint('publisher', __name__, url_prefix='/publishers')


@publisher_bp.route('/')
def list():
    
    # データ取得
    publishers = Publisher.select()

    return render_template('publisher_list.html', title='ユーザー一覧', items=publishers)


@publisher_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        Publisher.create(name=name, number=number)
        return redirect(url_for('publisher.list'))
    
    return render_template('publisher_add.html')


@publisher_bp.route('/edit/<int:publisher_id>', methods=['GET', 'POST'])
def edit(publisher_id):
    publisher = Publisher.get_or_none(Publisher.id == publisher_id)
    if not publisher:
        return redirect(url_for('publisher.list'))

    if request.method == 'POST':
        publisher.name = request.form['name']
        publisher.number = request.form['number']
        publisher.save()
        return redirect(url_for('publisher.list'))

    return render_template('publisher_edit.html', publisher=publisher)