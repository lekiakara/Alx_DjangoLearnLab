from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# -----------------------------
# FUNCTION-BASED VIEW
# -----------------------------
def book_list_view(request):
    """Display all books with their authors."""
    books = Book.objects.select_related('author').all()

    # Option 1: Plain text output
    # output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    # return HttpResponse(output, content_type="text/plain")

    # Option 2 (Recommended): Render HTML template
    return render(request, "relationship_app/book_list.html", {"books": books})



# -----------------------------
# CLASS-BASED VIEW
# -----------------------------
class LibraryDetailView(DetailView):
    """Display details for a specific library, including all books."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    # Add books to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
