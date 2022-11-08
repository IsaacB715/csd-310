import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n-- Main Menu --")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4) Exit Program")

    try:
        choice = int(input("Type in a number to choose a menu option: "))
        return choice

    except ValueError:
        print("\n An invalid entry occurred, closing program...")
        sys.exit(0)

def show_books(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = cursor.fetchall()

    print("\n-- DISPLAYING BOOK LISTING --")

    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))

def show_locations(_cursor):

    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

def validate_user():

    try:
        user_id = int(input("\nPlease enter your user ID: "))

        if user_id < 0 or user_id > 3:
            print("\nInvalid user ID, program terminated...\n")
            sys.exit(0)

        return user_id

    except ValueError:
        print("\nInvalid entry, program terminated...\n")
        sys.exit(0)

def show_account_menu():
    
    try:
        print("\n--Customer Menu --")
        print("\n1. Wishlist\n2. Add Book\n3. Main Menu")

        account_menu_option_chosen = int(input("Type in a number to choose a menu option: "))

        return account_menu_option_chosen

    except ValueError:
        print("\nInvalid menu option, program terminated...\n")
        sys.exit(0)

def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()

    print("\n --DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("\nBook Name: {}\nAuthor: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor,_user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n-- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("\nBook ID: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor,_user_id,_book_id):

    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("\nWelcome to the WhatABook Application!")

    user_selection = show_menu()

    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)
        
        if user_selection == 2:
            show_locations(cursor)
        
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("\nEnter the book ID of the book you want to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()

                    print("\nBook ID: {} was added to your wishlist!".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please try again...")

                account_option = show_account_menu()

        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please try again...")

        user_selection = show_menu()
    print("\n\nProgram terminated...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
