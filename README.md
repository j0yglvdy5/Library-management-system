# Library Management System

This project is a command-line interface (CLI) based Library Management System implemented in Python. It allows you to manage authors, books, and borrowers in a library system using SQLAlchemy for database management and Alembic for database migrations.

## Features

- Add new authors and books to the library.
- Track borrowers and which books they have borrowed.
- List all authors, books, and borrowers stored in the system.


### Important Files

#### `library/cli.py`

This file defines the command-line interface (CLI) for the Library Management System using Click. The CLI commands allow users to interact with the system easily. Here are the main commands:

- **`add_author_command(name)`**: Adds a new author to the library. Takes the author's name as an argument.
- **`add_book_command(title, author_id)`**: Adds a new book to the library. Takes the book title and the author's ID as arguments.
- **`add_borrower_command(name, book_id)`**: Adds a new borrower to the system. Takes the borrower's name and the book ID as arguments.
- **`list_authors_command()`**: Lists all authors in the library.
- **`list_books_command()`**: Lists all books in the library.
- **`list_borrowers_command()`**: Lists all borrowers and the books they have borrowed.

The `cli` function uses Click to group these commands together, providing a simple and intuitive interface for users.

#### `library/db.py`

This file is responsible for setting up the database connection and session. It contains the following key components:

- **`engine`**: Creates a SQLAlchemy engine connected to the SQLite database.
- **`SessionLocal`**: A SQLAlchemy sessionmaker bound to the engine, used to create database sessions.
- **`Base`**: The base class for all SQLAlchemy models, used to define the database schema.

#### `library/models.py`

This file defines the database models using SQLAlchemy ORM. Each class represents a table in the database:

- **`Author`**: Represents an author in the library. Has an `id` and a `name`, and a relationship with the `Book` model.
- **`Book`**: Represents a book in the library. Has an `id`, `title`, and a foreign key `author_id` linking to the `Author` model. Also has a relationship with the `Borrower` model.
- **`Borrower`**: Represents a borrower in the system. Has an `id`, `name`, and a foreign key `book_id` linking to the `Book` model.

#### `library/services.py`

This file contains functions that interact with the database, performing CRUD operations:

- **`get_db()`**: Provides a database session for use in other functions.
- **`add_author(name)`**: Adds a new author to the database.
- **`add_book(title, author_id)`**: Adds a new book to the database.
- **`add_borrower(name, book_id)`**: Adds a new borrower to the database.
- **`list_authors()`**: Returns a list of all authors in the database.
- **`list_books()`**: Returns a list of all books in the database.
- **`list_borrowers()`**: Returns a list of all borrowers in the database.

### Setup

### Prerequisites

- Python 3.10 or later
- Pipenv (for managing dependencies)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/j0yglvdy5/Library-management-system.git
   cd Library-management-system

