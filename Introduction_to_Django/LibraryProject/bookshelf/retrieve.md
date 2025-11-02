from bookshelf.models import Book

# Retrieve and display all books
books = Book.objects.get()
books
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell>]>

# Display all attributes of the first book
book = books.first()
book.id, book.title, book.author, book.publication_year
# Expected Output:
# (1, '1984', 'George Orwell', 1949)
