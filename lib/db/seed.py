from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Author, Book, Borrower

DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    author = Author(name="J.K. Rowling")
    db.add(author)
    db.commit()
    db.refresh(author)
    
    book = Book(title="Harry Potter and the Philosopher's Stone", author_id=author.id)
    db.add(book)
    db.commit()
    db.refresh(book)

    borrower = Borrower(name="John Doe")
    db.add(borrower)
    db.commit()
    db.refresh(borrower)

if __name__ == "__main__":
    init_db()
    seed_data()
