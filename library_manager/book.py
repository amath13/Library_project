# library_manager/book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
