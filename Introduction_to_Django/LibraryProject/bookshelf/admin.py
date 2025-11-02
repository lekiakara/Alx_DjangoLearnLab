from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Basic registration (enables admin access)
# admin.site.register(Book)

# Customized admin display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filtering sidebar by publication year or author
    list_filter = ('publication_year', 'author')

    # Add a search box for title or author
    search_fields = ('title', 'author')
