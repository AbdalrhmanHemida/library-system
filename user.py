class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)

    def is_borrowed(self, book):
        for mybook in self.borrowed_books:
            if mybook.id == book.id:
                return True
        return False

    def __repr__(self):
        ret = f'User name: {self.name:15} - id: {self.id}\n\tBorrowed books:\n'
        for book in self.borrowed_books:
            ret += f'\t{str(book)}\n'
        return ret