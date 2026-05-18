def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    else:
        print(f"Book {book_id} is not available.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"{book_id}: {title} by {author} ({year})")


catalog = {}
borrowed_books = []
members = set()

add_book(catalog, 101, "Python Basics", "Carol", 2020)
add_book(catalog, 102, "Data Structures", "Joe", 2021)
add_book(catalog, 103, "Machine Learning", "Terry", 2022)
add_book(catalog, 104, "Cloud Computing", "James", 2023)

register_member(members, 1)
register_member(members, 2)
register_member(members, 1)

borrow_book(catalog, borrowed_books, 101)
borrow_book(catalog, borrowed_books, 103)

return_book(borrowed_books, 101)

show_available(catalog, borrowed_books)

print("\nRegistered Members:", members)
print("Borrowed Books:", borrowed_books)