from peewee import Model, ForeignKeyField, DateField
from .db import db
from .user import User
from .book import Book

class Borrow(Model):
    user = ForeignKeyField(User, backref='borrows')
    book = ForeignKeyField(Book, backref='borrows')
    borrow_date = DateField()
    return_date = DateField(null=True)

    class Meta:
        database = db