from backend import BackendManger
from helper_functions.helper_methods import *
from typing import List, Tuple


class FrontendManager:
    def __init__(self) -> None:
        self.backend = BackendManger()

    def print_menu(self) -> int:
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

    def run(self) -> None:
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

    def add_user(self) -> None:
        print('\nEnter user info:')
        name = input('User name: ')
        id = input('User id: ')
        self.backend.add_user(name, id)

    def add_book(self) -> None:
        print('\nEnter book info:')
        name = input('Book name: ')
        id = input('Book id: ')
        total_quantity = int(input('Total quantity: '))
        self.backend.add_book(name, id, total_quantity)

    def print_users(self) -> None:
        users_str = '\n'.join([str(user) for user in self.backend.users])
        print(users_str)

    def print_books(self) -> None:
        # Let's "delegate" the call to a general function
        self.print_name_prefix(just_print_all=True)

    def print_name_prefix(self, just_print_all=False) -> None:
        prefix = ''
        if not just_print_all:
            prefix = input('Enter book name prefix: ')

        books = self.backend.get_books_with_prefix(prefix)
        books_str = '\n'.join([str(book) for book in books])
        print(books_str)

    def read_user_name_and_book_name(self, trials=3) -> Tuple[str, str]:
        """
        The function tries to read valid user name and password up to #trials
        If finally correct, it returns the read names, otherwise None, None
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

    def borrow_book(self) -> None:
        user_name, book_name = self.read_user_name_and_book_name()

        if user_name is None or book_name is None:
            return

        if not self.backend.borrow_book(user_name, book_name):
            print('Failed to borrow the book')

    def return_book(self) -> None:
        user_name, book_name = self.read_user_name_and_book_name()

        if user_name is None or book_name is None:
            return

        self.backend.return_book(user_name, book_name)

    def print_users_borrowed_book(self) -> None:
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
