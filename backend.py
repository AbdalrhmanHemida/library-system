from Book import Book
from user import User


class BackendManger:
    """A class for managing the backend of a library system.

       Attributes:
           books (list[Book]): A list of books in the library.
           users (list[User]): A list of users in the library.

       Methods:
           add_user(name: str, id: str) -> None:
               Adds a new user to the library system.

           add_book(name: str, id: str, total_quantity: int) -> None:
               Adds a new book to the library system.

           get_books_with_prefix(prefix: str) -> List[Book]:
               Returns a list of books whose names start with a given prefix.

           get_user_by_name(name: str) -> Optional[User]:
               Returns the user with the given name, or None if not found.

           get_book_by_name(name: str) -> Optional[Book]:
               Returns the book with the given name, or None if not found.

           borrow_book(user_name: str, book_name: str) -> bool:
               Borrows a book for a user.

           return_book(user_name: str, book_name: str) -> None:
               Returns a borrowed book to the library.

           get_users_borrowed_book(book_name: str) -> List[User]:
               Returns a list of users who have borrowed a book.

       """

    def __init__(self):
        """Initializes a new instance of the BackendManager class."""
        self.books = []
        self.users = []

    def add_user(self, name, id):
        """
          Adds a new user to the library system.

          Parameters
          ----------
          name : str
              The name of the user.
          id : str
              The unique identifier of the user.
        """
        self.users.append(User(name, id))

    def add_book(self, name, id, total_quantity):
        """
           Adds a new book to the library system.

           Parameters
           ----------
           name : str
               The name of the book.
           id : str
               The unique identifier of the book.
           total_quantity : int
               The total number of copies of the book in the library.
       """
        self.books.append(Book(name, id, total_quantity))

    def get_books_with_prefix(self, prefix):
        """
           Returns a list of books whose names start with the given prefix.

           Parameters
           ----------
           prefix : str
               The prefix to search for.

           Returns
           -------
           list of Book
               A list of Book objects whose names start with the given prefix.
       """
        return [book for book in self.books if book.name.startswith(prefix)]

    def get_user_by_name(self, name):
        """
           Returns a User object with the given name.

           Parameters
           ----------
           name : str
               The name of the user to search for.

           Returns
           -------
           User or None
               The User object with the given name if found, otherwise None.
       """
        for user in self.users:
            if name == user.name:
                return user
        return None

    def get_book_by_name(self, name):
        """
            Returns a Book object with the given name.

            Parameters
            ----------
            name : str
                The name of the book to search for.

            Returns
            -------
            Book or None
                The Book object with the given name if found, otherwise None.
        """
        for book in self.books:
            if name == book.name:
                return book
        return None

    def borrow_book(self, user_name, book_name):
        """
            Allows a user to borrow a book from the library system.

            Parameters
            ----------
            user_name : str
                The name of the user who wants to borrow the book.
            book_name : str
                The name of the book to be borrowed.

            Returns
            -------
            bool
                True if the book is successfully borrowed, False otherwise.
        """
        user = self.get_user_by_name(user_name)
        book = self.get_book_by_name(book_name)

        if user is None or book is None:
            return False

        if book.borrow():
            user.borrow(book)
            return True
        return False

    def return_book(self, user_name, book_name):
        """
          Returns a borrowed book to the library.

          Parameters
          ----------
          user_name : str
              The name of the user who is returning the book.
          book_name : str
              The name of the book that is being returned.
        """
        user = self.get_user_by_name(user_name)
        book = self.get_book_by_name(book_name)

        if user is None or book is None:
            return

        if user.is_borrowed(book):
            book.return_copy()
            user.return_book(book)
        else:
            print('This user did not borrow this book')

    def get_users_borrowed_book(self, book_name):
        """
         Returns a list of all users who borrowed a specific book.

         Parameters
         ----------
         book_name : str
             The name of the book for which the list of users is being returned.

         Returns
         -------
         List[User]
             A list of all users who borrowed the specified book.
             An empty list is returned if the book does not exist in the library.
        """
        book = self.get_book_by_name(book_name)

        if book is None:
            return []

        return [user for user in self.users if user.is_borrowed(book)]
