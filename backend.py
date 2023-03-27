from book import Book
from user import User
from typing import List, Optional


class BackendManger:
    def __init__(self) -> None:
        self.books = []
        self.users = []

    def add_user(self, name: str, id: str) -> None:
        self.users.append(User(name, id))

    def add_book(self, name: str, id: str, total_quantity: int) -> None:
        self.books.append(Book(name, id, total_quantity))

    def get_books_with_prefix(self, prefix: str) -> List[Book]:
        return [book for book in self.books if book.name.startswith(prefix)]

    def get_user_by_name(self, name: str) -> Optional[User]:
        for user in self.users:
            if name == user.name:
                return user
        return None

    def get_book_by_name(self, name: str) -> Optional[Book]:
        for book in self.books:
            if name == book.name:
                return book
        return None

    def borrow_book(self, user_name: str, book_name: str) -> bool:
        user = self.get_user_by_name(user_name)
        book = self.get_book_by_name(book_name)

        if user is None or book is None:
            return False

        if book.borrow():
            user.borrow(book)
            return True
        return False

    def return_book(self, user_name: str, book_name: str) -> None:
        user = self.get_user_by_name(user_name)
        book = self.get_book_by_name(book_name)

        if user is None or book is None:
            return

        if user.is_borrowed(book):
            book.return_copy()
            user.return_book(book)
        else:
            print('This user did not borrow this book')

    def get_users_borrowed_book(self, book_name: str) -> List[User]:
        book = self.get_book_by_name(book_name)

        if book is None:
            return []

        return [user for user in self.users if user.is_borrowed(book)]