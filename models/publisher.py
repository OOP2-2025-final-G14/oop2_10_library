from peewee import Model, CharField, IntegerField
from .db import db

class Publisher(Model):
    name = CharField()
    number = IntegerField()

    class Meta:
        database = db
