from __future__ import unicode_literals
from ..books_app.models import Book
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length = 50)
    books = models.ManyToManyField(Book, related_name = 'published_books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
