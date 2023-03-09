from db.models import Author, CookBook, Recipe

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']
CATEGORIES = ["breakfast", 
                "desserts", 
                "soups and stews",
                "sides dishes", 
                "salads and dressings", 
                "sauces and dips",
                "main dishes"
]

def create_author_table(authors):
    print('-' * 80)
    print(f'|ID  |FIRST-NAME{" " * 25}|LAST-NAME{" " * 28}|')
    print('-' * 80)
    for author in authors:
        id_spaces = 4 - len(str(author.id))
        first_name_spaces = 35 - len(author.first_name) 
        last_name_spaces =  37- len(author.last_name)
        print(f'|{author.id}{" " * id_spaces}|{author.first_name}{" " * first_name_spaces}|{author.last_name}{" " * last_name_spaces}|')
    print('-' * 80)


def create_cook_book_table(author):
    print('-' * 85)
    print(f'|ID  |BOOK NAME{" " * 41}|AUTHOR{" " * 21}|')
    print('-' * 85)
    for cook_book in sorted(author.books, key=lambda b: b.id):
        id_spaces = 4 - len(str(cook_book.id))
        name_spaces = 50 - len(cook_book.name)
        author_spaces = 26 - len(author.first_name + author.last_name)
        output_string = f'|{cook_book.id}{" " * id_spaces}|' + \
            f'{cook_book.name}{" " * name_spaces}|' + \
            f'{author.first_name} {author.last_name}{" " * author_spaces}|'

        print(output_string)
    print('-' * 85)

def create_receipe_table(recipes):
    print('-' * 80)
    print(f'|ID  |RECEIPE LINK{" " * 24}|CATEGORY{" " * 28}|')
    print('-' * 80)
    for recipe in sorted(recipes, key=lambda b: b.id):
        id_spaces = 4 - len(str(recipe.id))
        link_spaces = 36 - len(recipe.link)
        category_spaces = 36 - len(recipe.category)
        output_string = f'|{recipe.id}{" " * id_spaces}|' + \
            f'{recipe.link}{" " * link_spaces}|' + \
            f'{recipe.category}{" " * category_spaces}|' 

        print(output_string)
    print('-' * 80)



def show_all_cookbooks(session, books):
    print('-' * 80)
    print(f'|ID  |COOKBOOK NAME{" " * 37}|AUTHOR{" " * 16}|')
    print('-' * 80)
    for book in sorted(books, key=lambda b: b.id):
        author = session.query(Author).get(book.author_id)
        id_spaces = 4 - len(str(book.id))
        book_spaces = 50 - len(book.name)
        author_spaces = 21 - (len(author.first_name) + len(author.last_name))
        output_string = f'|{book.id}{" " * id_spaces}|' + \
            f'{book.name}{" " * book_spaces}|' + \
            f'{author.first_name} {author.last_name}{" " * author_spaces}|'

        print(output_string)
    print('-' * 80)


def main_menu():
    print("Here is the menu:")
    print("Enter 1 to check recipe types.")
    print("Enter 2 to check all authors.")
    print("Enter 3 to check all cookbooks.")
    print("Enter 'exit' to quit.")
    
    choice = input("Please enter: ")
    
    return choice



def show_category():
    print('-' * 80)
    print(f'|CATEGORY{" " * 70}|')
    print('-' * 80)
    for ca in CATEGORIES:
        ca_spaces = 78 - len(ca)
        output_string = f"|{ca}{' ' * ca_spaces}|"
        print(output_string)
    print('-' * 80)

    yes_no = input("Enter category name to continue searching or enter 'no' to go back to main menu: ")
    return yes_no
    


def check_category(session, chosen_category):
    recipes = session.query(Recipe).all()
    chosen_recipes = []
    for recipe in recipes:
        if recipe.category == chosen_category:
            chosen_recipes.append(recipe)
    
    create_receipe_table(chosen_recipes)