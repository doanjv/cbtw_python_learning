class Book:
    """Represents a book in the library."""
    def __init__(self, book_id, title, author, isbn, is_borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book ID: {self.book_id} | Title: '{self.title}' | Author: {self.author} | Status: {status}"

class User:
    """Represents a user/patron of the library."""
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  

    def __str__(self):
        return f"User ID: {self.user_id} | Name: {self.name} | Books Borrowed: {len(self.borrowed_books)}"

    def borrow_book(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)