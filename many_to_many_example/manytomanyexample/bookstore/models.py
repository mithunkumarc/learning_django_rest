from django.db import models

class Author(models.Model):
	name = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 300)

class Book(models.Model):
	title = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 300)
	authors = models.ManyToManyField(Author)
