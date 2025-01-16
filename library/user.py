class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return f"{self.name} borrowed {book.title}"
        return f"{book.title} is not available"

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}"
        return f"{self.name} doesn't have {book.title}"

    def __str__(self):
        return f"User: {self.name}, Borrowed books: {', '.join([b.title for b in self.borrowed_books])}"
