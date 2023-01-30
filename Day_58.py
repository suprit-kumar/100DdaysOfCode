"""
Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can print all books,
add a book and get the number of books using different methods.
Show that your program doesn't persist the books after the program is stopped!
"""


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        self.books.append(book)
        print(f"All Books: {self.books}")
    def books_count(self):
        print(f"Total books count: {len(self.books)}")


addBook = Library()
addBook.add_book("physics")
addBook.books_count()