from peewee import Model, CharField, ForeignKeyField
from .db import db
from .publisher import Publisher

class Book(Model):
    title = CharField()
    author = CharField()
    publisher = ForeignKeyField(Publisher, backref='books')

    class Meta:
        database = db
