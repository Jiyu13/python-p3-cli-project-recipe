#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Author, CookBook
from helpers import (create_author_table, create_cook_book_table, 
                     create_receipe_table, show_all_cookbooks, 
                     show_category, main_menu,
                     check_category)

engine = create_engine('sqlite:///db/recipes.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('''
 ____  ____   ___  ____  ____  ____     ___  __    ____ 
(  _ \( ___) / __)(_  _)(  _ \( ___)   / __)(  )  (_  _)
 )   / )__) ( (__  _)(_  )___/ )__)   ( (__  )(__  _)(_ 
(_)\_)(____) \___)(____)(__)  (____)   \___)(____)(____)                            
    ''')


is_game_on = True
# menu
while is_game_on:
    choice = main_menu()
    print("\n")
    if choice == "2":
        print('Here is a list of available authors:')
        authors = session.query(Author)
        create_author_table(authors)

        # Get a choice of author, retrieve an object from the DB
        author = None
        print("\n")
        while not author:
            try:
                author_id = int(input('Please enter the ID of the author to check his/her cookbooks: '))
            except:
                print("!!!!!please enter a valid ID!!!!!")
            
            else: 
                if 1<= int(author_id) <= authors.count():
                    author = session.query(Author).filter(Author.id == author_id).one_or_none()
                    
                else:
                    print("!!!!!please enter a correct ID!!!!!")

        # Display list of cookbooks written by the author
        print('Here is a list of cookbooks: ')
        create_cook_book_table(author)

        cook_book = None
        while not cook_book:
            print("\n")

            cook_book_id = input('Please enter the ID of the cookbook to check recipes: ')
            cookbooks = session.query(CookBook).filter(CookBook.author_id==cook_book_id)
            
            cook_book = session.query(CookBook).filter(CookBook.id == cook_book_id).one_or_none()

        # Display the receipes inside the cookbook
        print('Here are the recipes in this cookbook: ')
        create_receipe_table(cook_book.recipes)

    elif choice == "3":
        all_cookbooks = None
        is_check_recipe = True
        while is_check_recipe:
            cookbooks = session.query(CookBook)
            book_id = show_all_cookbooks(session, cookbooks)
            if book_id == "#":
                is_check_recipe = False
            elif 1 <= int(book_id) <= cookbooks.count():
                cookbook = session.query(CookBook).filter(CookBook.id==is_check_recipe).one_or_none()
                create_receipe_table(cookbook.recipes)
            else:
                print("!!!!!please enter a valid ID!!!!!")

        
    elif choice == "1":
        in_category = True
        while in_category:
            yes_no = show_category()

            if yes_no != "no":
                check_category(session, yes_no)
            else:
                in_category = False

    elif choice == "exit":
        is_game_on = False
        print("Bye!")
    
    else:
        print("!!!!!please enter a valid command!!!!!")
        print("\n")