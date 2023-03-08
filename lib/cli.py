#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Author, CookBook
from helpers import (create_author_table, create_cook_book_table, create_receipe_table)

engine = create_engine('sqlite:///db/recipes.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('Hello! Welcome to the Receipe CLI.')
    print('Here is a list of available authors:')
    authors = session.query(Author)
    create_author_table(authors)

# Get a choice of author, retrieve an object from the DB
    author = None
    while not author:
        author_id = input('Please enter the ID of the author: ')
        author = session.query(Author).filter(Author.id == author_id).one_or_none()

    # Display list of cookbooks written by the author
    print('Here is a list of cookbooks: ')
    create_cook_book_table(author)

    cook_book = None
    while not cook_book:
        cook_book_id = input('Please enter the ID of the cookbook: ')
        cook_book = session.query(CookBook).filter(CookBook.id == cook_book_id).one_or_none()

    # Display the receipes inside the cookbook
    print('Here are the receipies in this cookbook: ')
    create_receipe_table(cook_book)