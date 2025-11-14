from django.shortcuts import render

# Create your views here.

# Function-Based View

def list_books(request):
    """
    A function-based view that lists all books and their authors.
    """

    books = Book.objects.select_related("author").all()

    # Simple text output
    output = "List of Books:\n\n"
    for book in books:
        output += f"- {book.title} by {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")



# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"



