from peewee import Model, CharField
from .db import db

class Publisher(Model):
    name = CharField()

    class Meta:
        database = db