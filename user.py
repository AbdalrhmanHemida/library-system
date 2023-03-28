class User:
    """
        A class representing a user of a library.

        Attributes
        ----------
        name : str
           The name of the user.
        id : str
           The unique identifier of the user.
        borrowed_books : list of Book objects
           The list of books borrowed by the user.

        Methods
        -------
        borrow(book)
           Adds a book to the user's borrowed_books list.
        is_borrowed(book)
           Returns True if the user has borrowed the given book, False otherwise.
        return_book(book)
           Removes a book from the user's borrowed_books list.
        simple_repr(is_detailed = False)
           Returns a string representation of the user's information.
        __repr__()
           Returns a detailed string representation of the user's information.
    """
    def __init__(self, name, id):
        """
            Constructs a new User object.

            Parameters
            ----------
            name : str
              The name of the user.
            id : str
              The unique identifier of the user.
        """
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow(self, book):
        """
            Adds a new borrowed book to the user's list of borrowed books.

            Parameters
            ----------
            book : Book
              The book object to be added to the user's list of borrowed books.
        """
        self.borrowed_books.append(book)

    def is_borrowed(self, book):
        """
            Checks whether the user has borrowed the specified book.

            Parameters
            ----------
            book : Book
              The book object to be checked.

            Returns
            -------
            bool
              True if the user has borrowed the specified book, False otherwise.
        """
        for mybook in self.borrowed_books:
            if mybook.id == book.id:
                return True
        return False

    def return_book(self, book):
        """
            Removes the specified borrowed book from the user's list of borrowed books.

            Parameters
            ----------
            book : Book
              The book object to be removed from the user's list of borrowed books.
        """
        for idx, mybook in enumerate(self.borrowed_books):
            if mybook.id == book.id:
                del self.borrowed_books[idx]
                break

    def simple_repr(self, is_detailed = False):
        """
            Returns a string representation of the user.

            Parameters
            ----------
            is_detailed : bool, optional
               Whether to include detailed information about the user's borrowed books,
               by default False.

            Returns
            -------
            str
               A string representation of the user.
       """
        ret = f'User name: {self.name:15} - id: {self.id}'
        if is_detailed and self.borrowed_books:
            ret += '\n\tBorrowed books:\n'
            for book in self.borrowed_books:
                ret += f'\t{str(book)}\n'
        return ret

    def __repr__(self):
        """
            Returns a detailed string representation of the user.

            Returns
            -------
            str
               A detailed string representation of the user.
       """
        return self.simple_repr(True)
