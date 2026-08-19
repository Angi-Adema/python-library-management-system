# Library management system prompting a user to add books including title, author, and
# number of copies, managing the process of borrowing a book, returning borrowed books, and 
# displaying book inventory.

# Create a list to store dictionaries of books
from random import choice


book_inventory = [
    # Store a few books to establish the initial inventory
    {
        "title": "Harry Potter and the Half-Blood Prince",
        "author": "J.K. Rowling",
        "copies": 5
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "copies": 3
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "copies": 4
    }
]

# Create a function for the main menu of the library management system including a menu prompt
# and passing in the book inventory as a parameter to be utilized by the function called within the main menu function.
def main_menu(inventory):
    while True:
        print("\n    Library Management System    ")
        print("----------------------------------")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Display Book Inventory")
        print("5. Exit")

        option = input("\n Please enter your choice (1-5): ")

        # Call add_new_book() function if the user selects option 1
        if option == '1':
            add_new_book(inventory)

        # Call borrow_book() function if the user selects option 2
        elif option == '2':
            borrow_book(inventory)

        # Call return_book() function if the user selects option 3
        elif option == '3':
            return_book(inventory)

        # Call display_inventory() function if the user selects option 4
        elif option == '4':
            display_inventory(inventory)

        # Exit the program if the user selects option 5
        elif option == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# REFERENCES
#
# 1. GeeksforGeeks. (2025, July 23). "How to create list of dictionary in Python". 
#    https://www.geeksforgeeks.org/python/how-to-create-list-of-dictionary-in-python/
# 2. Miller, B. (n.d.). "Programming in Python 3" zyBooks, a Wiley Brand.
#    Canvas https://www.zybooks.com/




