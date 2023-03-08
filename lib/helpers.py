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

# def create_cook_book_table(author):
#     print('-' * 50)
#     print(f'|ID  |BOOK NAME{" " * 20}|LINK{" " * 4}|CATEGORY{" " * 4}')
#     print('-' * 50)
#     for cook_book in sorted(author.books, key=lambda b: b.id):
#         id_spaces = 4 - len(str(cook_book.id))
#         name_spaces = 33 - len(cook_book.name)
#         output_string = f'|{cook_book.id}{" " * id_spaces}|' + \
#             f'{cook_book.name}{" " * name_spaces}|'

#         print(output_string)
#     print('-' * 50)

# link_spaces = 33 - len(cook_book.link)
# category_spaces = 33 - len(cook_book.category)
            #  + \
    # f'{cook_book.link}{" " * link_spaces}|' + \
    # f'{cook_book.category}{" " * category_spaces}|' 

def fill_cart(session, author):
    shopping_cart = ShoppingCart(author=author)
    cook_book_id = input('Please enter the ID of your first item: ')
    cart_total = 0
    while cook_book_id:
        cook_book = session.query(GroceryItem).filter(
            GroceryItem.id==cook_book_id).first()
        if cook_book in author.cook_books:
            shopping_cart.cook_books.append(cook_book)
            cart_total += cook_book.price
            print(f'Cart total is now ${cart_total:.2f}\n')
        else:
            cook_book_id = input('Please enter a valid grocery item ID: ')
            continue

        yes_no = None
        while yes_no not in YES + NO:
            yes_no = input('Would you like to add another item to your cart? (Y/n) ')
            if yes_no.lower() in YES:
                cook_book_id = input('Please enter the ID of your next item: ')
            elif yes_no.lower() in NO:
                cook_book_id = None

    return shopping_cart, cart_total

def show_cart(shopping_cart):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 29}|PRICE{" " * 4}|')
    print('-' * 50)
    for cook_book in sorted(shopping_cart.cook_books, key=lambda g: g.id):
        id_spaces = 4 - len(str(cook_book.id))
        name_spaces = 33 - len(cook_book.name)
        price_spaces = 8 - len(f'{cook_book.price:.2f}')
        output_string = f'|{cook_book.id}{" " * id_spaces}|' + \
            f'{cook_book.name}{" " * name_spaces}|' + \
            f'${cook_book.price:.2f}{" " * price_spaces}|'
        print(output_string)
    cart_total = sum([g.price for g in shopping_cart.cook_books])
    total_spaces = 8 - len(str(cart_total))
    print(f'|{" " * 5}TOTAL{" " * 28}|${cart_total:.2f}{" " * total_spaces}|')
    print('-' * 50)

def remove_from_cart(session, shopping_cart, cart_total):
    yes_no = input('Would you like to remove any items from your cart? (Y/n) ')
    while yes_no in YES:
        cook_book_id = input('Please enter the ID of the item you would like to remove: ')
        cook_book = session.query(GroceryItem).filter(
            GroceryItem.id==cook_book_id).first()
        if cook_book in shopping_cart.cook_books:
            shopping_cart.cook_books.remove(cook_book)
            cart_total -= cook_book.price
        else:
            print('Item not found.')
        print('Here are the items in your cart:')
        show_cart(shopping_cart)

        yes_no = input('Would you like to remove another item from your cart? (Y/n) ')

def collect_payment(cart_total):
    paid = False
    while not paid:
        payment_method = input(f'Will you be paying with cash or card? ')
        if payment_method.lower() == 'card':
            print('Processing...\n')
            paid = True
        elif payment_method.lower() == 'cash':
            payment = input('How much will you be paying with today? ' )
            try:
                payment = float(payment)
                change = payment - cart_total
                print(f'Your change is ${change:.2f}\n')
                paid = True
            except:
                print('Please enter a valid number.')
        else:
            print('Please select a valid payment method.')
