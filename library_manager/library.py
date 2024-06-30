# library_manager/library.py
from .book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def lend_book(self, title):
        book = self.find_book(title)
        if book and book.available:
            book.available = False
            return True
        return False

    def return_book(self, title):
        book = self.find_book(title)
        if book and not book.available:
            book.available = True
            return True
        return False
