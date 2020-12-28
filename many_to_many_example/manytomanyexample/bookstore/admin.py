from django.contrib import admin
from .models import Author, Book
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # list all fields in table(Admin UI)
    list_display = ['name', 'desc']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list all fields in table(Admin UI)
    list_display = ['title', 'desc']
