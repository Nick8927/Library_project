from library.book import Book
from library.user import LibraryUser

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added book: {book}"

    def register_user(self, user):
        self.users.append(user)
        return f"Registered user: {user.name}"

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if len(available_books) <= 0:
            return "We haven't the books"
        return "Available books:\n" + "\n".join(str(book) for book in available_books)
