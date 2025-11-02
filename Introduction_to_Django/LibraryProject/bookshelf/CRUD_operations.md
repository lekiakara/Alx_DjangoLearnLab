from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output confirmation
book
# Expected Output:
# <Book: 1984 by George Orwell>


from bookshelf.models import Book

# Retrieve and display all books
books = Book.objects.all()
books
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell>]>

# Display all attributes of the first book
book = books.first()
book.id, book.title, book.author, book.publication_year
# Expected Output:
# (1, '1984', 'George Orwell', 1949)

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
Book.objects.get(id=book.id)
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell>

from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected Output:
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
