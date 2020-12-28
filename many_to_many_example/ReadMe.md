#### ManyToManyExample : 

        Author : might have written many books
        Book : might have written by many authors
  
        third table created with many to many mappings between book and author

##### test in admin ui , postman test not covered

#### 1. create root project

        django-admin startproject manytomanyexample

#### 2. create app bookstore 

        cd manytomanyexample
        python manage.py startapp bookstore

#### 3. add rest_framework and bookstore to project : manytomanyexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'bookstore',
        ]


#### 4. bookstore/models.py

        from django.db import models 

        class Author(models.Model): 
          name = models.CharField(max_length = 100) 
          desc = models.TextField(max_length = 300) 

        class Book(models.Model): 
          title = models.CharField(max_length = 100) 
          desc = models.TextField(max_length = 300) 
          authors = models.ManyToManyField(Author) 


#### 5. register in bookstore/admin.py 

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


#### 5. create and apply schema

        python manage.py makemigrations
        python manage.py migrate

        python manage.py createsuperuser
        admin 
        c0met123

        python manage.py runserver

#### 6. test : login to localhost:8000/admin

        in admin ui : try to add books and authors and map them
        create two authors
        create two books, each book add both authors 

#### 7. open: db.sqlite3 file in https://sqliteonline.com/

        open table : bookstore_book_authors
