import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Author, CookBook, Recipe

CATEGORIES = ["breakfast", 
                "desserts", 
                "soups and stews",
                "sides dishes", 
                "salads and dressings", 
                "sauces and dips",
                "main dishes"
]

engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()


def make_authors():
    print("Deleting existing authors...")
    session.query(Author).delete()
    session.commit()

    authors = [Author(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    ) for i in range(5)]

    session.add_all(authors)
    session.commit()
    return authors
    

def make_cook_books(authors):
    print("Deleting existing books...")
    session.query(CookBook).delete()
    session.commit()

    cook_books = []
    for author in authors:
        for i in range(random.randint(1, 3)):
            book = CookBook(
                name=fake.unique.text().split(".")[0],
                author_id=author.id
            )
            cook_books.append(book)

    session.add_all(cook_books)
    session.commit()
    return cook_books


def make_recipes(cook_books):
    print("Deleting existing recipes...")
    session.query(Recipe).delete()
    session.commit()

    recipes = []
    for book in cook_books:
        for i in range(random.randint(5, 10)):
            recipe = Recipe(
                category=random.choice(CATEGORIES),
                link=fake.url(),
                book_id=book.id
            )
            recipes.append(recipe)

    session.add_all(recipes)
    session.commit()
    return recipes


if __name__ == '__main__':

    authors = make_authors()
    books = make_cook_books(authors)
    make_recipes = make_recipes(books)
    
    # engine = create_engine('sqlite:///recipes.db')
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # fake = Faker()

    # session.query(Author).delete()
    # session.query(CookBook).delete()
    # session.query(Recipe).delete()


    # CATEGORIES = ["breakfast", 
    #             "desserts", 
    #             "soups and stews"
    #             "sides dishes", 
    #             "salads and dressings", 
    #             "sauces and dips"
    #             "main dishes"
    # ]

    # authors = []
    # for i in range(5):
    #     author = Author(
    #         first_name=fake.unique.firstName(),
    #         last_name=fake.unique.lastName()
    #     )

    #     session.add(author)
    #     session.commit()
    #     authors.append(author)

    
    # cook_books = []
    # for author in authors:
    #     for i in range(rc(1, 3))
    #         book = CookBook(
    #             name=fake.unique.text().split(".")[0]
    #             author_id=author.id
    #         )
    #         cook_books.append(book)
