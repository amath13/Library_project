# main.py
from library_manager.book import Book
from library_manager.library import Library
from library_manager.book_database import BookDatabase

def main():
    # Création d'une instance de BookDatabase
    book_db = BookDatabase()

    # Charger les livres depuis la base de données
    books_data = book_db.load_books()

    # Création d'une bibliothèque
    library = Library()

    # Ajouter les livres chargés à la bibliothèque
    for book_data in books_data:
        book = Book(book_data['title'], book_data['author'])
        book.available = book_data['available']  # Mettre à jour la disponibilité
        library.add_book(book)

    # Ajouter quelques livres supplémentaires
    book1 = Book("Harry Potter", "J.K. Rowling")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Affichage de la liste des livres dans la bibliothèque
    print("List of books in the library:")
    for book in library.books:
        print(book)

    # Exemple de recherche de livre
    search_title = "Harry Potter"
    found_book = library.find_book(search_title)
    if found_book:
        print(f"Book found: {found_book}")
    else:
        print(f"Book '{search_title}' not found in the library.")

    # Exemple de prêt de livre
    book_to_lend = "The Lord of the Rings"
    if library.lend_book(book_to_lend):
        print(f"Book '{book_to_lend}' has been lent.")
    else:
        print(f"Book '{book_to_lend}' is not available for lending.")

    # Exemple de retour de livre
    book_to_return = "The Lord of the Rings"
    if library.return_book(book_to_return):
        print(f"Book '{book_to_return}' has been returned.")
    else:
        print(f"Book '{book_to_return}' is not currently borrowed.")

    # Sauvegarder les livres dans la base de données
    books_to_save = [{'title': book.title, 'author': book.author, 'available': book.available} for book in library.books]
    book_db.save_books(books_to_save)

if __name__ == "__main__":
    main()
