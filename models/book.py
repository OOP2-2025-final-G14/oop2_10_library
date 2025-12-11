from peewee import Model, CharField, IntegerField, ForeignKeyField
from .db import db
from .publisher import Publisher


class Book(Model):
    title = CharField()                 # 本のタイトル
    author = CharField()                # 著者名
    publisher = ForeignKeyField(Publisher, backref='books')  # 出版社
    
    class Meta:
        database = db