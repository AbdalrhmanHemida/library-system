from backend import BackendManger
from helper_functions.helper_methods import *


class FrontendManager:
    def __init__(self):
        self.backend = BackendManger()

    def print_menu(self):
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
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.add_book()
            # elif choice == 2:
            #     self.print_books()
            # elif choice == 3:
            #     self.print_name_prefix()
            # elif choice == 4:
            #     self.add_user()
            # elif choice == 5:
            #     self.borrow_book()
            # elif choice == 6:
            #     self.return_book()
            # elif choice == 7:
            #     self.print_users_borrowed_book()
            # elif choice == 8:
            #     self.print_users()
            else:
                break

    def add_user(self):
        print('\nEnter user info:')
        name = input('User name: ')
        id = input('User id: ')
        self.backend.add_user(name, id)

    def add_book(self):
        print('\nEnter book info:')
        name = input('Book name: ')
        id = input('Book id: ')
        total_quantity = int(input('Total quantity: '))
        self.backend.add_book(name, id, total_quantity)
