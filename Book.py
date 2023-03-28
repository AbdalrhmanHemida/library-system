from typing import List, Optional


class Book:
    """
        Represents a book in a library system.

        Attributes
        ----------
        name : str
            The name of the book.
        id : str
            The unique identifier of the book.
        total_quantity : int
            The total number of copies of the book in the library.
        total_borrowed : int
            The number of copies of the book that are currently borrowed.

        Methods
        -------
        borrow()
            Borrow a copy of the book.
        return_copy()
            Return a borrowed copy of the book.
        __repr__()
            Return a string representation of the book.

    """
  
    def __init__(self, name: str, id: str, total_quantity: int) -> None:
         """
          Constructs a new Book object.

          Parameters
          ----------
          name : str
              The name of the book.
          id : str
              The unique identifier of the book.
          total_quantity : int
              The total number of copies of the book in the library.
        """
        
        self.name = name
        self.id = id
        self.total_quantity = total_quantity
        self.total_borrowed = 0

    def borrow(self) -> bool:
        """
          Borrow a copy of the book.

          Returns
          -------
          bool
              True if the book was successfully borrowed, False otherwise.
        """
        
        if self.total_quantity - self.total_borrowed == 0:
              return False
          self.total_borrowed += 1
          return True

    def return_copy(self) -> None:
        """
           Return a borrowed copy of the book.

           Raises
           ------
           AssertionError
               If there are no copies currently borrowed.
        """
      
        assert self.total_borrowed > 0
        self.total_borrowed -= 1

    def __repr__(self):
        """
            Return a string representation of the book.

            Returns
            -------
            str
                A formatted string including the name, id, total quantity, and total borrowed attributes.
        """
        
        return f'Book name: {self.name:20} - id: {self.id} - total quantity: {self.total_quantity} - ' \
               f'total borrowed: {self.total_borrowed}'
