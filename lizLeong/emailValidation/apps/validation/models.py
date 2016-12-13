from __future__ import unicode_literals

from django.db import models
import datetime
import re

# Create your models here.
class EmailManager(models.Manager):
  def validate(self, email):
      valid_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
      if valid_email.match(email): ##add stoof here
        data ={
            'email':email,
        }
        return data
      else:
          data={
            'error': 'Invalid email format, try again >:(',
          }
          return data

          #   class UserManager(models.Manager):
          #   def login(self, postData):
          #       print "Running a login function!"
          #       print "If successful login occurs, maybe return {'theuser':user} where user is a user object?")
          #       print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
          #       pass
          #   def register(self, postData):
          #       print ("Register a user here")
          #       print ("If successful, maybe return {'theuser':user} where user is a user object?")
          #       print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
          #       pass

class Email(models.Model):
    email = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailManager()
