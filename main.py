from library.library import Library
from library.book import Book
from library.user import LibraryUser

def main():
    library = Library()
    library.add_book(Book("1984", "George Orwell", 1949))
    # library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))

    user = LibraryUser("Alice")
    library.register_user(user)

    print(library.list_available_books())
    print(user.borrow_book(library.books[0]))
    print(library.list_available_books())
    print(user.return_book(library.books[0]))
    # print(library.list_available_books())

if __name__ == "__main__":
    main()
