from helper_functions.helper_methods import *


class FrontendManager:
    def __init__(self):
        pass

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
