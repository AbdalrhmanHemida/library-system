class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def __repr__(self):
        ret = f'User name: {self.name:15} - id: {self.id}\n\tBorrowed books:\n'
        for book in self.borrowed_books:
            ret += f'\t{str(book)}\n'
        return ret