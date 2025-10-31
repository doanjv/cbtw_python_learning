from library_manager import Library 

library = Library()

print("Add Books and Users")
library.add_book("The Clean Coder", "Robert C. Martin", "978-0137081073")
library.add_book("Tam quoc dien nghia", "La Quan Trung", "978-1449340377") 
library.add_book("Anh hung xa dieu", "Kim Dung", "978-0743273565")

library.add_user("Alice Johnson")
library.add_user("Bob Smith")

print("View Entities")
library.view_all_books()
library.view_all_users()

print("Perform Borrowing/Returning")
print("\n--- Borrow Operation ---")
library.borrow_book(user_id=1, book_id=1) # Alice borrows The Clean Coder
library.borrow_book(user_id=2, book_id=3) # Bob borrows The Great Gatsby

print("\n--- Attempt to re-borrow ---")
library.borrow_book(user_id=2, book_id=1) # Fails: already borrowed

print("\n--- Return Operation ---")
library.return_book(user_id=1, book_id=1) # Alice returns The Clean Coder

print("Search books that is by 'Robert C. Martin' AND is NOT borrowed")
search_criteria = lambda book: "Robert C. Martin" in book.author and not book.is_borrowed
available_martin_books = library.search_books(search_criteria)

if available_martin_books:
    for book in available_martin_books:
        print(f"Found: {book}")
else:
    print("No matching books found.")

print("Search Users has more than 0 borrowed books")
search_criteria_users = lambda user: len(user.borrowed_books) > 0
users_with_loans = library.search_users(search_criteria_users)

if users_with_loans:
    for user in users_with_loans:
        print(f"Found: {user}")
else:
    print("No users currently have loans.")