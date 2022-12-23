from book import Book
from user import User


class BackendManger:
    def __init__(self):
        self.books = []
        self.users = []

    def add_user(self, name, id):
        self.users.append(User(name, id))
