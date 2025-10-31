from library_entities import Book, User 

class Library:
    """Manages the collection of books and users, and handles operations."""
    def __init__(self):
        self._books = {}  
        self._users = {} 
        self._next_book_id = 1
        self._next_user_id = 1

    def add_book(self, title, author, product_code):
        book_id = self._next_book_id
        new_book = Book(book_id, title, author, product_code)
        self._books[book_id] = new_book
        self._next_book_id += 1
        print(f"✅ Added book: {new_book}")

    def add_user(self, name):
        user_id = self._next_user_id
        new_user = User(user_id, name)
        self._users[user_id] = new_user
        self._next_user_id += 1
        print(f"✅ Added user: {new_user}")

    def view_all_books(self):
        print("\n--- All Books ---")
        if not self._books:
            print("No books in the library.")
            return
        for book in self._books.values():
            print(book)

    def view_all_users(self):
        print("\n--- All Users ---")
        if not self._users:
            print("No users registered.")
            return
        for user in self._users.values():
            print(user)

    def borrow_book(self, user_id, book_id):
        user = self._users.get(user_id)
        book = self._books.get(book_id)

        if not user:
            print(f"❌ Error: User ID {user_id} not found.")
        elif not book:
            print(f"❌ Error: Book ID {book_id} not found.")
        elif book.is_borrowed:
            print(f"❌ Error: Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            user.borrow_book(book_id)
            print(f"✨ Successfully borrowed '{book.title}' by User: {user.name}")

    def return_book(self, user_id, book_id):
        user = self._users.get(user_id)
        book = self._books.get(book_id)

        if not user:
            print(f"❌ Error: User ID {user_id} not found.")
        elif not book:
            print(f"❌ Error: Book ID {book_id} not found.")
        elif not book.is_borrowed:
            print(f"❌ Error: Book '{book.title}' was not borrowed.")
        elif book_id not in user.borrowed_books:
             print(f"❌ Error: User {user.name} did not borrow book '{book.title}'.")
        else:
            book.is_borrowed = False
            user.return_book(book_id)
            print(f"🎉 Successfully returned '{book.title}' by User: {user.name}")


    def search_books(self, predicate):
        """
        Searches books using a predicate function (Functional Programming inspiration).

        Example usage: search_books(lambda book: 'Python' in book.title and not book.is_borrowed)
        """
        return list(filter(predicate, self._books.values()))

    def search_users(self, predicate):
        """
        Searches users using a predicate function (Functional Programming inspiration).
        """
        return list(filter(predicate, self._users.values()))