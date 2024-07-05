from sqlalchemy.orm import Session
from lib.db.models import Author, Book, Borrower

def create_author(db: Session, name: str):
    db_author = Author(name=name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    return db.query(Author).all()

def update_author(db: Session, author_id: int, name: str):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db_author.name = name
        db.commit()
        db.refresh(db_author)
        return db_author
    return None

def delete_author(db: Session, author_id: int):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
        return db_author
    return None

