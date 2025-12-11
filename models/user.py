from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    # 手動でIDを設定できるように変更
    id = IntegerField(primary_key=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db