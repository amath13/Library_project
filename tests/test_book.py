# test_book.py
import pytest
from library_manager.book import Book

def test_book_creation():
    book = Book("Harry Potter", "J.K. Rowling")
    assert book.title == "Harry Potter"
    assert book.author == "J.K. Rowling"
    assert book.available is True
