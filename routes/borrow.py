from flask import Blueprint, render_template, request, redirect, url_for
from models import Borrow, User, Book
from datetime import date

borrow_bp = Blueprint('borrow', __name__, url_prefix='/borrow')


# 貸し出し一覧
@borrow_bp.route('/')
def list():
    borrows = Borrow.select()
    return render_template('borrow_list.html', borrows=borrows)


# 貸し出し登録
@borrow_bp.route('/add', methods=['GET', 'POST'])
def add():
    users = User.select()
    books = Book.select()

    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        book_id = int(request.form['book_id'])
        borrow_date = request.form.get('borrow_date')
        return_date = request.form.get('return_date') or None

        Borrow.create(
            user=user_id,
            book=book_id,
            borrow_date=borrow_date,
            return_date=return_date
        )
        return redirect(url_for('borrow.list'))

    return render_template(
        'borrow_add.html',
        users=users,
        books=books,
        today=date.today()
    )


# 編集
@borrow_bp.route('/edit/<int:borrow_id>', methods=['GET', 'POST'])
def edit(borrow_id):
    borrow = Borrow.get_or_none(Borrow.id == borrow_id)
    if not borrow:
        return redirect(url_for('borrow.list'))

    users = User.select()
    books = Book.select()

    if request.method == 'POST':
        borrow.user = int(request.form['user_id'])
        borrow.book = int(request.form['book_id'])
        borrow.borrow_date = request.form.get('borrow_date')
        return_date = request.form.get('return_date') or None
        borrow.return_date = return_date

        borrow.save()
        return redirect(url_for('borrow.list'))

    return render_template(
        'borrow_edit.html',
        borrow=borrow,
        users=users,
        books=books,
        today=date.today()
    )


# 削除
@borrow_bp.route('/delete/<int:borrow_id>')
def delete(borrow_id):
    borrow = Borrow.get_or_none(Borrow.id == borrow_id)
    if borrow:
        borrow.delete_instance()

    return redirect(url_for('borrow.list'))



# 返却（return_date を今日に変更）
@borrow_bp.route('/return/<int:borrow_id>')
def do_return(borrow_id):
    borrow = Borrow.get_or_none(Borrow.id == borrow_id)
    if borrow:
        borrow.return_date = date.today()
        borrow.save()

    return redirect(url_for('borrow.list'))
