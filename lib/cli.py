import click
from .services import add_author, add_book, add_borrower, list_authors, list_books, list_borrowers

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def add_author_command(name):
    add_author(name)
    click.echo(f'Author {name} added.')

@click.command()
@click.argument('title')
@click.argument('author_id')
def add_book_command(title, author_id):
    add_book(title, author_id)
    click.echo(f'Book "{title}" added.')

@click.command()
@click.argument('name')
@click.argument('book_id')
def add_borrower_command(name, book_id):
    add_borrower(name, book_id)
    click.echo(f'Borrower {name} added.')

@click.command()
def list_authors_command():
    authors = list_authors()
    for author in authors:
        click.echo(f'{author.id}: {author.name}')

@click.command()
def list_books_command():
    books = list_books()
    for book in books:
        click.echo(f'{book.id}: {book.title} by {book.author.name}')

@click.command()
def list_borrowers_command():
    borrowers = list_borrowers()
    for borrower in borrowers:
        click.echo(f'{borrower.id}: {borrower.name} borrowed "{borrower.book.title}"')

cli.add_command(add_author_command, name='add-author')
cli.add_command(add_book_command, name='add-book')
cli.add_command(add_borrower_command, name='add-borrower')
cli.add_command(list_authors_command, name='list-authors')
cli.add_command(list_books_command, name='list-books')
cli.add_command(list_borrowers_command, name='list-borrowers')
