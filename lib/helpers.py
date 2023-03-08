from db.models import Author, CookBook, Recipe

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']

def create_author_table(authors):
    print('-' * 37)
    print(f'|ID  |FIRST-NAME{" " * 5}|LAST-NAME{" " * 5}|')
    print('-' * 37)
    for author in authors:
        id_spaces = 4 - len(str(author.id))
        first_name_spaces = 15 - len(author.first_name) 
        last_name_spaces = 14 - len(author.last_name)
        print(f'|{author.id}{" " * id_spaces}|{author.first_name}{" " * first_name_spaces}|{author.last_name}{" " * last_name_spaces}|')
    print('-' * 37)


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

def create_receipe_table(book):
    print('-' * 80)
    print(f'|ID  |RECEIPE LINK{" " * 24}|CATEGORY{" " * 28}|')
    print('-' * 80)
    for recipe in sorted(book.recipes, key=lambda b: b.id):
        id_spaces = 4 - len(str(recipe.id))
        link_spaces = 36 - len(recipe.link)
        category_spaces = 36 - len(recipe.category)
        output_string = f'|{recipe.id}{" " * id_spaces}|' + \
            f'{recipe.link}{" " * link_spaces}|' + \
            f'{recipe.category}{" " * category_spaces}|' 

        print(output_string)
    print('-' * 80)
