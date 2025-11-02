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
