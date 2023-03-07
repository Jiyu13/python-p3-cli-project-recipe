from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Author, CookBook, Recipe

engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def make_authors():
    session.query(Author).delete()
    session.commit()

    authors = [Author(
        first_name=fake.firstName(),
        last_name=fake.lastName(),
    ) for i in range[20]]

    session.add_all(authors)
    session.commit()

    return authors

def make_cook_books():
    session.query(CookBook).delete()
    session.commit()

    cook_books = [CookBook(
        name=fake.name(),
        quantity=rc(10, 25),
        price=rc(10, 25)
    )for i in range(20)]
    session.add_all(cook_books)
    session.commit()

    return cook_books


def make_receipes():
    session.query(Recipe).delete()
    session.commit()

    receipes = [Recipe(
        name=fake.name(),
        category=fake.word(),
        link=fake.url(),
    ) for i in range(50)]

    session.add_all(receipes)
    session.commit()

    return receipes
