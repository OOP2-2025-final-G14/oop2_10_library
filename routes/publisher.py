from flask import Blueprint, render_template, request, redirect, url_for
from models import Publisher

publisher_bp = Blueprint('publisher', __name__, url_prefix='/publishers')

@publisher_bp.route('/')
def list():
    publishers = Publisher.select()
    return render_template('publisher_list.html', title='出版社一覧', items=publishers)

@publisher_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        Publisher.create(name=name)
        return redirect(url_for('publisher.list'))
    return render_template('publisher_add.html')

@publisher_bp.route('/edit/<int:publisher_id>', methods=['GET', 'POST'])
def edit(publisher_id):
    publisher = Publisher.get_or_none(Publisher.id == publisher_id)
    if not publisher:
        return redirect(url_for('publisher.list'))
    if request.method == 'POST':
        publisher.name = request.form['name']
        publisher.save()
        return redirect(url_for('publisher.list'))
    return render_template('publisher_edit.html', publisher=publisher)