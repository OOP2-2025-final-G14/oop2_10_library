from flask import Blueprint, render_template, request, redirect, url_for
from models import Book, Publisher

book_bp = Blueprint('book', __name__, url_prefix='/books')

@book_bp.route('/')
def list():
    books = Book.select()
    return render_template('book_list.html', title='本一覧', items=books)

@book_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publisher_id = request.form.get('publisher_id')  # 空の可能性あり
        published_year = request.form.get('published_year') or None
        isbn = request.form.get('isbn') or None

        publisher = None
        if publisher_id:
            publisher = Publisher.get_or_none(Publisher.id == int(publisher_id))

        Book.create(
            title=title,
            author=author,
            publisher=publisher,
            published_year=(int(published_year) if published_year else None),
            isbn=isbn
        )
        return redirect(url_for('book.list'))

    publishers = Publisher.select()
    return render_template('book_add.html', publishers=publishers)

@book_bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = Book.get_or_none(Book.id == book_id)
    if not book:
        return redirect(url_for('book.list'))

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        publisher_id = request.form.get('publisher_id')
        book.published_year = int(request.form.get('published_year')) if request.form.get('published_year') else None
        book.isbn = request.form.get('isbn') or None

        if publisher_id:
            book.publisher = Publisher.get_or_none(Publisher.id == int(publisher_id))
        else:
            book.publisher = None

        book.save()
        return redirect(url_for('book.list'))

    publishers = Publisher.select()
    return render_template('book_edit.html', book=book, publishers=publishers)