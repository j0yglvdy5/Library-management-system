import click
from library.services import (
    add_author,
    add_book,
    add_borrower,
    list_authors,
    list_books,
    list_borrowers,
    delete_author,
    delete_book,
    delete_borrower,
    find_author_by_name,
    find_book_by_title,
    find_borrower_by_name
)

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def add_author_command(name):
    add_author(name)

@click.command()
@click.argument('title')
@click.argument('author_id', type=int)
def add_book_command(title, author_id):
    add_book(title, author_id)

@click.command()
@click.argument('name')
@click.argument('book_id', type=int)
def add_borrower_command(name, book_id):
    add_borrower(name, book_id)

@click.command()
def list_authors_command():
    authors = list_authors()
    for author in authors:
        click.echo(f"{author.id}: {author.name}")

@click.command()
def list_books_command():
    books = list_books()
    for book in books:
        click.echo(f"{book.id}: {book.title} (Author ID: {book.author_id})")

@click.command()
def list_borrowers_command():
    borrowers = list_borrowers()
    for borrower in borrowers:
        click.echo(f"{borrower.id}: {borrower.name} (Book ID: {borrower.book_id})")

@click.command()
@click.argument('author_id', type=int)
def delete_author_command(author_id):
    delete_author(author_id)

@click.command()
@click.argument('book_id', type=int)
def delete_book_command(book_id):
    delete_book(book_id)

@click.command()
@click.argument('borrower_id', type=int)
def delete_borrower_command(borrower_id):
    delete_borrower(borrower_id)

@click.command()
@click.argument('name')
def find_author_command(name):
    author = find_author_by_name(name)
    if author:
        click.echo(f"Author ID: {author.id}, Name: {author.name}")
    else:
        click.echo("Author not found.")

@click.command()
@click.argument('title')
def find_book_command(title):
    book = find_book_by_title(title)
    if book:
        click.echo(f"Book ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}")
    else:
        click.echo("Book not found.")

@click.command()
@click.argument('name')
def find_borrower_command(name):
    borrower = find_borrower_by_name(name)
    if borrower:
        click.echo(f"Borrower ID: {borrower.id}, Name: {borrower.name}, Book ID: {borrower.book_id}")
    else:
        click.echo("Borrower not found.")

cli.add_command(add_author_command, name='add-author')
cli.add_command(add_book_command, name='add-book')
cli.add_command(add_borrower_command, name='add-borrower')
cli.add_command(list_authors_command, name='list-authors')
cli.add_command(list_books_command, name='list-books')
cli.add_command(list_borrowers_command, name='list-borrowers')
cli.add_command(delete_author_command, name='delete-author')
cli.add_command(delete_book_command, name='delete-book')
cli.add_command(delete_borrower_command, name='delete-borrower')
cli.add_command(find_author_command, name='find-author')
cli.add_command(find_book_command, name='find-book')
cli.add_command(find_borrower_command, name='find-borrower')

if __name__ == '__main__':
    cli()
