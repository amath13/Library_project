# test_integration.py
import pytest
from library_manager.library import Library
from library_manager.book import Book

@pytest.fixture
def library_with_books():
    library = Library()
    book1 = Book("Harry Potter", "J.K. Rowling")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
    library.add_book(book1)
    library.add_book(book2)
    return library

def test_library_find_book(library_with_books):
    book = library_with_books.find_book("Harry Potter")
    assert book.title == "Harry Potter"

def test_library_lend_book(library_with_books):
    assert library_with_books.lend_book("The Lord of the Rings") is True

def test_library_return_book(library_with_books):
    library_with_books.lend_book("The Lord of the Rings")
    assert library_with_books.return_book("The Lord of the Rings") is True
