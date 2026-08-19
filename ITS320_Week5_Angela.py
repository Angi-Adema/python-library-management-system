# Library management system prompting a user to add books including title, author, and
# number of copies, managing the process of borrowing a book, returning borrowed books, and 
# displaying book inventory.

# Create a list to store dictionaries of books and their title, author, and number of copies
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
# and passing in the book inventory as a parameter to be utilized by the functions called within the main menu function.
def main_menu(inventory):
    while True:
        print("\n    Library Management System    ")
        print("----------------------------------")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Display Book Inventory")
        print("5. Exit")

        option = input("\nPlease enter your choice (1-5): ").strip()

        # Call add_new_book(inventory) function if the user selects option 1
        if option == '1':
            add_new_book(inventory)

        # Call borrow_book(inventory) function if the user selects option 2
        elif option == '2':
            borrow_book(inventory)

        # Call return_book(inventory) function if the user selects option 3
        elif option == '3':
            return_book(inventory)

        # Call display_inventory(inventory) function if the user selects option 4
        elif option == '4':
            display_inventory(inventory)

        # Exit the program if the user selects option 5
        elif option == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Search inventory and return book dictionary if found, otherwise return None
def book_search(inventory, title):

    # Loop through the book_inventory list to see if a book title exists
    for book in inventory:

        # Ensure the search is case-insensitive by converting both the book title and the search title to lowercase
        if book["title"].lower() == title.lower():

            # If book is found, return the book dictionary
            return book

    # Return None if the book does not exist in the inventory
    return None

# Create a function to add a new book to the inventory
def add_new_book(inventory):
    # Validate title input.
    while True:
        # Prompt user to enter the title of the book to be added to inventory removing any leading or trailing whitespace from the input
        title = input("Please enter the book title: ").strip()

        # Validate the input to ensure the title is not empty
        if title == "":
            print("\nBook title cannot be empty. Please enter a valid title.")
        else:       
            # Check to see if the title is already in the inventory by calling the book_search function
            exists_in_inventory = book_search(inventory, title)

            # If the book already exists in the inventory, request the user to enter a different title
            if exists_in_inventory is not None:
                print(f"\nThe book '{title}' already exists in the inventory. Please enter a different title.")
            else:
                # If the title is valid and does not already exist in the inventory, break out of the loop
                break

    # Validate author input.
    while True:
        # Prompt user to enter the author's name removing any leading or trailing whitespace from the input   
        author = input("Enter the book author: ").strip()

        # Validate the input to ensure the author's name is not empty
        if author == "":
            print("\nAuthor name cannot be empty. Please enter a valid author name.")
        else:
            # If the author's name is valid, break out of the loop
            break

    # Validate copies input.
    while True:
        # Utilize try-except for validation
        try:
            # Prompt user to enter the number of copies of the book removing any leading or trailing whitespace from the input
            copies = int(input("Enter the number of copies: ").strip())

            # Validate input is a positive integer
            if copies <= 0:
                print("\nNumber of copies must be greater than zero. Please enter a valid number.")
            else:
                # Exit the loop if the input is valid
                break

        # Display message if input is not a valid integer
        except ValueError:
            print("\nInvalid input. Please enter a valid positive integer for the number of copies.")

    # Create a dictionary for the new book
    new_book = {
        "title": title,
        "author": author,
        "copies": copies
    }

    # Append the new book dictionary to the inventory list
    inventory.append(new_book)

    # Display a message confirming the book has been added to the inventory
    print(f"\nBook '{title}' by {author} has been successfully added to the inventory.")

# Create a function to handle borrowing a book from the inventory
def borrow_book(inventory):
    # Continue prompting until the user enters a nonempty title
    while True:
        # Prompt the user to enter the title of the book they wish to borrow removing any leading or trailing whitespace from the input
        title = input("Enter the title of the book you want to borrow: ").strip()

        # Validate the input was not empty
        if title == "":
            print("\nBook title cannot be empty. Please enter a valid title.")
        else:
            # Call the book_search function to check if the book exists in the inventory
            book = book_search(inventory, title)

            # If the book is found in the inventory
            if book is not None:
                # Check if there are copies available to borrow
                if book["copies"] > 0:
                    # Decrease the number of copies by 1
                    book["copies"] -= 1

                    # Display a message confirming the book has been borrowed
                    print(f"\nYou have successfully borrowed '{book['title']}' by {book['author']}.")
                else:
                    # Display a message indicating that there are no copies available to borrow
                    print(f"\nSorry, '{book['title']}' by {book['author']} is currently out of stock.")
            else:
                # Display a message indicating that the book was not found in the inventory
                print(f"\nSorry, '{title}' is not available in the inventory.")

            # Exit the loop after processing a nonempty title
            break

# Create a function to handle returning a book
def return_book(inventory):
    # Reprompt the user to enter a nonempty book title
    while True:
        # Prompt the user to enter the title of the book they wish to return removing any leading or trailing whitespace from the input
        title = input("Enter the title of the book you want to return: ").strip()

        # Validate the input was not empty
        if title == "":
            print("\nBook title cannot be empty. Please enter a valid title.")
        else:
            # Call the book_search function to check if the book exists in the inventory
            book = book_search(inventory, title)

            # If the book is found in the inventory
            if book is not None:
                # Increase the number of copies by 1
                book["copies"] += 1

                # Display a message confirming the book has been returned
                print(f"\nYou have successfully returned '{book['title']}' by {book['author']}.")
            else:
                # Display a message indicating that the book was not found in the inventory
                print(f"\nSorry, '{title}' is not recognized in our inventory. Please check the title and try again.")

            # Exit the loop after processing a nonempty title
            break

# Create a function to display the current book inventory
def display_inventory(inventory):
    # Check if the inventory is empty
    if not inventory:
        print("\nThe book inventory is currently empty.")
    else:
        # Display the book inventory in a formatted manner
        print("\nCurrent Book Inventory:")
        print("------------------------")
        for book in inventory:
            print(f"Title: {book['title']}, Author: {book['author']}, Copies Available: {book['copies']}")

# Call the main_menu function to start the library management system
main_menu(book_inventory)


# REFERENCES
#
# 1. GeeksforGeeks. (2025, July 23). "How to create list of dictionary in Python". 
#    https://www.geeksforgeeks.org/python/how-to-create-list-of-dictionary-in-python/
# 2. GeeksforGeeks. (2025, July 11). "Remove spaces from a string in Python". 
#    https://www.geeksforgeeks.org/python/python-remove-spaces-from-a-string/
# 3. GeeksforGeeks. (2026, May 29). "Python Exception Handling".
#    https://www.geeksforgeeks.org/python/python-exception-handling/
# 4. GeeksforGeeks. (2025, July 26). "Parentheses, Square Brackets and Curly Braces in Python".
#    https://www.geeksforgeeks.org/python/parentheses-square-brackets-and-curly-braces-in-python/
# 5. Miller, B. (n.d.). "Programming in Python 3" zyBooks, a Wiley Brand.
#    Canvas https://www.zybooks.com/





