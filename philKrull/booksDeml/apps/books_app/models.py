from __future__ import unicode_literals

from django.db import models
# to use bcrypt
import bcrypt
# Create your models here.
class authorManager(models.Manager):
    def add_author(self, postData):
        errors = []
        if not len(postData['name']):
            errors.append('Author must have a name!')
        response = {}
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(name=postData['name'])
        return response

class Author(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = authorManager()

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, related_name= 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
