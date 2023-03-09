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

    if choice == "2":
        print('Here is a list of available authors:')
        authors = session.query(Author)
        create_author_table(authors)

        # Get a choice of author, retrieve an object from the DB
        author = None
        while not author:
            author_id = input('Please enter the ID of the author to check his/her cookbooks: ')
            author = session.query(Author).filter(Author.id == author_id).one_or_none()

        # Display list of cookbooks written by the author
        print('Here is a list of cookbooks: ')
        create_cook_book_table(author)

        cook_book = None
        while not cook_book:
            cook_book_id = input('Please enter the ID of the cookbook to check recipes: ')
            cook_book = session.query(CookBook).filter(CookBook.id == cook_book_id).one_or_none()

        # Display the receipes inside the cookbook
        print('Here are the recipes in this cookbook: ')
        create_receipe_table(cook_book.recipes)


        # is_continue = True
        # while is_continue:
        # print("Would you want to go back to the main menu or exit?")
        # command = input("Enter 1 to go back to main menu, 0 to exit: ")
        # if command == "0":
        #     is_game_on = False
        # elif command == "1":
        #     main_menu()
        # else:
        #     print('Please enter a valid command.')


    elif choice == "3":
        all_cookbooks = None
        is_check_recipe = True
        while is_check_recipe:
            cookbooks = session.query(CookBook).all()
            is_check_recipe = show_all_cookbooks(session, cookbooks)
            if is_check_recipe == "#":
                is_check_recipe = False
            else:
                cookbook = session.query(CookBook).filter(CookBook.id==is_check_recipe).one_or_none()
                create_receipe_table(cookbook.recipes)

        
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