import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.helpers import create_author, get_authors, update_author, delete_author

DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def add_author(name):
    db = SessionLocal()
    author = create_author(db, name)
    click.echo(f"Added author: {author.name}")

@click.command()
def list_authors():
    db = SessionLocal()
    authors = get_authors(db)
    for author in authors:
        click.echo(f"{author.id}: {author.name}")

@click.command()
@click.argument('author_id')
@click.argument('name')
def update_author_cmd(author_id, name):
    db = SessionLocal()
    author = update_author(db, author_id, name)
    if author:
        click.echo(f"Updated author: {author.name}")
    else:
        click.echo(f"Author with id {author_id} not found")

@click.command()
@click.argument('author_id')
def delete_author_cmd(author_id):
    db = SessionLocal()
    author = delete_author(db, author_id)
    if author:
        click.echo(f"Deleted author: {author.name}")
    else:
        click.echo(f"Author with id {author_id} not found")

cli.add_command(add_author)
cli.add_command(list_authors)
cli.add_command(update_author_cmd)
cli.add_command(delete_author_cmd)

if __name__ == '__main__':
    cli()
