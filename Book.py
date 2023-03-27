class Book:
    def __init__(self, name: str, id: str, total_quantity: int) -> None:
        self.name = name
        self.id = id
        self.total_quantity = total_quantity
        self.total_borrowed = 0

    def borrow(self) -> bool:
        if self.total_quantity - self.total_borrowed == 0:
            return False
        self.total_borrowed += 1
        return True

    def return_copy(self) -> None:
        assert self.total_borrowed > 0
        self.total_borrowed -= 1

    def __repr__(self) -> str:
        return f'Book name: {self.name:20} - id: {self.id} - total quantity: {self.total_quantity} - ' \
               f'total borrowed: {self.total_borrowed}'
