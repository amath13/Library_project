# test_library.py
import pytest
from library_manager.library import Library
from library_manager.book import Book

@pytest.fixture
def empty_library():
    return Library()

def test_library_empty_on_creation(empty_library):
    assert len(empty_library.books) == 0

def test_library_add_book(empty_library):
    book = Book("To Kill a Mockingbird", "Harper Lee")
    empty_library.add_book(book)
    assert len(empty_library.books) == 1

def test_library_find_book(empty_library):
    book = Book("To Kill a Mockingbird", "Harper Lee")
    empty_library.add_book(book)
    found_book = empty_library.find_book("To Kill a Mockingbird")
    assert found_book == book

def test_library_lend_book(empty_library):
    book = Book("To Kill a Mockingbird", "Harper Lee")
    empty_library.add_book(book)
    assert empty_library.lend_book("To Kill a Mockingbird") is True

def test_library_return_book(empty_library):
    book = Book("To Kill a Mockingbird", "Harper Lee")
    empty_library.add_book(book)
    empty_library.lend_book("To Kill a Mockingbird")
    assert empty_library.return_book("To Kill a Mockingbird") is True
