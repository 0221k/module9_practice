from django.contrib import admin
from .models import Author, Book, BookType

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookType)