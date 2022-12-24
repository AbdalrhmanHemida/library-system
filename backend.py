from book import Book
from user import User


class BackendManger:
    def __init__(self):
        self.books = []
        self.users = []

    def add_user(self, name, id):
        self.users.append(User(name, id))

    def add_book(self, name, id, total_quantity):
        self.books.append(Book(name, id, total_quantity))

    def get_books_with_prefix(self, prefix):
        return [book for book in self.books if book.name.startswith(prefix)]

    def get_user_by_name(self, name):
        for user in self.users:
            if name == user.name:
                return user
        return None

    def get_book_by_name(self, name):
        for book in self.books:
            if name == book.name:
                return book
        return None
