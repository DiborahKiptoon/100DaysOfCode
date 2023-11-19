class Author:
    def __init__(self, author_name):
        self.author_name = author_name

    def __str__(self):
        return self.author_name


class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id})"


class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def display_catalog(self):
        print("Library Catalog:")
        for book in self.catalog:
            print(book)

    def borrow_book(self, book_id):
        for book in self.catalog:
            if book.book_id == book_id:
                if book.available:
                    print(f"Book '{book.title}' borrowed successfully.")
                    book.available = False
                else:
                    print(f"Book '{book.title}' is not available.")
                return
        print("Book not found in the catalog.")


# Example usage
if __name__ == "__main__":
    # Creating authors
    author1 = Author("J.K. Rowling")
    author2 = Author("George Orwell")

    # Creating books
    book1 = Book("Harry Potter and the Sorcerer's Stone", author1, 1)
    book2 = Book("1984", author2, 2)

    # Creating a library
    library = Library()

    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Displaying the library catalog
    library.display_catalog()

    # Borrowing a book
    library.borrow_book(1)

    # Displaying the updated library catalog
    library.display_catalog()