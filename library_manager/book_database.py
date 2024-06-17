# book_database.py

class BookDatabase:
    def __init__(self, filename='books.csv'):
        self.filename = filename

    def load_books(self):
        books = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    title, author, available = line.strip().split(',')
                    book = {
                        'title': title,
                        'author': author,
                        'available': True if available == 'True' else False
                    }
                    books.append(book)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, on renvoie une liste vide
            pass

        return books

    def save_books(self, books):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for book in books:
                file.write(f"{book['title']},{book['author']},{book['available']}\n")

    def update_book_availability(self, title, available):
        books = self.load_books()
        for book in books:
            if book['title'] == title:
                book['available'] = available
                break
        self.save_books(books)

    def find_book_by_title(self, title):
        books = self.load_books()
        for book in books:
            if book['title'] == title:
                return book
        return None
