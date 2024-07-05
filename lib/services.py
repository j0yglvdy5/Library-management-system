
from sqlalchemy.orm import Session
from .db import SessionLocal
from lib.db.models import Author, Book, Borrower

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_author(name: str):
    db = next(get_db())
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)

def add_book(title: str, author_id: int):
    db = next(get_db())
    book = Book(title=title, author_id=author_id)
    db.add(book)
    db.commit()
    db.refresh(book)

def add_borrower(name: str, book_id: int):
    db = next(get_db())
    borrower = Borrower(name=name, book_id=book_id)
    db.add(borrower)
    db.commit()
    db.refresh(borrower)

def list_authors():
    db = next(get_db())
    return db.query(Author).all()

def list_books():
    db = next(get_db())
    return db.query(Book).all()

def list_borrowers():
    db = next(get_db())
    return db.query(Borrower).all()
