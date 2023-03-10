import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Author, CookBook, Recipe, User, cookbook_user

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

def make_users():
    print("Deleting existing authors...")
    session.query(User).delete()
    session.commit()

    users = [User(
        username=fake.simple_profile()["username"]
    ) for i in range(30)]

    session.add_all(users)
    session.commit()
    return users

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


def join_table(users, books):
    print("Deleting existing join-table...")
    session.query(cookbook_user).delete()
    session.commit()
    for book in books:
        for i in range(random.randint(1, 5)):
            user = random.choice(users)
            if book not in user.cookbooks:
                user.cookbooks.append(book)
                session.add(user)
                session.commit()


if __name__ == '__main__':

    authors = make_authors()
    books = make_cook_books(authors)
    make_recipes = make_recipes(books)
    users = make_users()
    join_table(users, books)

    # for user in users:
    #     for i in range(random.randint(1,3)):
    #         book = random.choice(books)
    #         if user not in book.users:
    #             book.users.append(user)
    #             session.add(book)
    #             session.commit()
        # # user.cookbooks[:] = []
        #     if user not in user.cookbooks:
            # user.cookbooks.append(random.choice(books))

    # session.bulk_save_objects(users)    
    # session.commit()
    