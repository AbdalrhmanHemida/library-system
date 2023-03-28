class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow(self, book: Book):
        self.borrowed_books.append(book)

    def is_borrowed(self, book: Book) -> bool:
        for mybook in self.borrowed_books:
            if mybook.id == book.id:
                return True
        return False

    def return_book(self, book: Book):
        for idx, mybook in enumerate(self.borrowed_books):
            if mybook.id == book.id:
                del self.borrowed_books[idx]
                break

    def simple_repr(self, is_detailed: bool = False) -> str:
        ret = f'User name: {self.name:15} - id: {self.id}'
        if is_detailed and self.borrowed_books:
            ret += '\n\tBorrowed books:\n'
            for book in self.borrowed_books:
                ret += f'\t{str(book)}\n'
        return ret

    def __repr__(self) -> str:
        return self.simple_repr(True)