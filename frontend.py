from backend import BackendManger
from helper_functions.helper_methods import *


class FrontendManager:
    """
        A class for managing the frontend of a library system.

        Attributes:
            backend (BackendManger): An instance of the BackendManger class.

        Methods:
            print_menu(): Prints the options menu and returns the user's choice as an integer.
            run(): Runs the library system and executes the corresponding function based on the user's choice.
            add_user(): Prompts the user to enter information for a new user and adds them to the library system.
            add_book(): Prompts the user to enter information for a new book and adds it to the library system.
            print_users(): Prints a list of all users in the library system.
            print_books(): Prints a list of all books in the library system.
            print_name_prefix(just_print_all=False): Prompts the user to enter a book name prefix, and prints a list of all books with that prefix.
            read_user_name_and_book_name(trials=3): Prompts the user to enter a valid username and bookname and returns the entered values as a tuple.
            borrow_book(): Prompts the user to enter a valid username and bookname to borrow a book.
            return_book(): Prompts the user to enter a valid username and bookname to return a book.
            print_users_borrowed_book(): Prompts the user to enter a valid book name and prints a list of all users who borrowed that book.
    """
    def __init__(self):
        self.backend = BackendManger()

    def print_menu(self):
        """
           Prints the options menu and returns the user's choice as an integer.

           Returns:
               int: The user's choice.
        """
        print('\nProgram Options:')

        messages = [
            'Add book',
            'Print library books',
            'Print books by prefix',
            'Add user',
            'Borrow book',
            'Return book',
            'Print users borrowed book',
            'Print users',
        ]
        messages = numbering_items(messages)
        print('\n'.join(messages))

        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        """
            Runs the library system and executes the corresponding function based on the user's choice.
        """
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.print_name_prefix()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed_book()
            elif choice == 8:
                self.print_users()
            else:
                break

    def add_user(self):
        """
            Prompts the user to enter information for a new user and adds them to the library system.
        """
        print('\nEnter user info:')
        name = input('User name: ')
        id = input('User id: ')
        self.backend.add_user(name, id)

    def add_book(self):
        """
           Prompts the user to enter information for a new book and adds it to the library system.
        """
        print('\nEnter book info:')
        name = input('Book name: ')
        id = input('Book id: ')
        total_quantity = int(input('Total quantity: '))
        self.backend.add_book(name, id, total_quantity)

    def print_users(self):
        """
            Prints a list of all users in the library system.
        """
        users_str = '\n'.join([str(user) for user in self.backend.users])
        print(users_str)

    def print_books(self):
        """
            Prints a list of all books in the library system.
            Prompts the user to enter a book name prefix to filter the list,
            but if just_print_all=True, it prints the entire list without prompting.
        """
        # Let's "delegate" the call to a general function
        self.print_name_prefix(just_print_all=True)

    def print_name_prefix(self, just_print_all=False):
        """
            Helper function that prints a list of books in the library system
            whose names begin with the specified prefix.
            If just_print_all is True, it prints the entire list without prompting
            for a prefix.
       """
        prefix = ''
        if not just_print_all:
            prefix = input('Enter book name prefix: ')

        books = self.backend.get_books_with_prefix(prefix)
        books_str = '\n'.join([str(book) for book in books])
        print(books_str)

    def read_user_name_and_book_name(self, trials=3):
        """
            Prompts the user to enter a valid user name and book name.
            It tries up to #trials times to read valid inputs.
            If successful, returns the user and book names.
            If not, returns None, None.
        """
        trials += 1

        while trials > 0:
            trials -= 1
            print('Enter user name and book name')

            user_name = input('User name: ')
            if self.backend.get_user_by_name(user_name) is None:
                print('Invalid user name!')
                continue

            book_name = input('Book name: ')
            if self.backend.get_book_by_name(book_name) is None:
                print('Invalid book name!')
                continue

            return user_name, book_name

        print('You did several trials! Try later.')
        return None, None

    def borrow_book(self):
        """
            Prompts the user to enter a valid user name and book name to borrow.
            If successful, borrows the book for the specified user.
            If not, prints a failure message.
        """
        user_name, book_name = self.read_user_name_and_book_name()

        if user_name is None or book_name is None:
            return

        if not self.backend.borrow_book(user_name, book_name):
            print('Failed to borrow the book')

    def return_book(self):
        """
            Prompts the user to enter a valid user name and book name to return.
            If successful, returns the book for the specified user.
            If not, prints a failure message.
        """
        user_name, book_name = self.read_user_name_and_book_name()

        if user_name is None or book_name is None:
            return

        self.backend.return_book(user_name, book_name)

    def print_users_borrowed_book(self):
        """
            Prompts the user to enter a book name and prints a list of users
            who have borrowed that book.
        """
        book_name = input('Book name: ')
        if self.backend.get_book_by_name(book_name) is None:
            print('Invalid book name!')
        else:
            users_lst = self.backend.get_users_borrowed_book(book_name)

            if not users_lst:
                print('\nNo one borrowed this book')
            else:
                print('\nList of users borrowed this book')
                for user in users_lst:
                    print(user.simple_repr())
