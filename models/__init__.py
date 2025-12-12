from .db import db
from .user import User
from .book import Book
from .borrow import Borrow
from .publisher import Publisher

MODELS = [
    User,
    Publisher,
    Book,
    Borrow
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()