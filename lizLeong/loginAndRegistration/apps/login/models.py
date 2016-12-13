from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

# Create your models here.

class validate(models.Manager):
    def validate(self, postData):
        errors = []
        response = {}
        valid_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not len(postData['first_name']) >= 2 or not len(postData['last_name']) >= 2:
            errors.append('**Names must be at least 2 characters**')
        if not valid_email.match(postData['email']):
            errors.append('**Please enter a valid email address**')
        if not len(postData['password']) >= 8:
            errors.append('**Password must be at least 8 characters**')
        if not postData['password'] == postData['password_confirmation']:
            errors.append('**Passwords didn\'t match**')
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            password = postData['password']
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hashed)
        return response
    def login(self, postData):
        errors = []
        response = {}
        user = User.objects.filter(email = postData['email']) # resolve more than one match with filter or try, except #also resolve incorrect email
        if not user:
            errors.append('**Email not found. Email is case sensitive. **')
            response['status'] = False
            response['errors'] = errors
            return response
        hashed = user[0].password
        check_password = bcrypt.hashpw(postData['password'].encode('utf-8'), hashed.encode('utf-8'))
        if not hashed == check_password:
            errors.append('**Incorrect password**')
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
        return response



class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    apdated_at = models.DateTimeField(auto_now = True)
    objects = validate()
