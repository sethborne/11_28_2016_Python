from __future__ import unicode_literals
from django.db import models
import bcrypt, re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[A-Za-z]{2,}$')
password_regex = re.compile(r'^[a-zA-Z0-9!@#$%^&*()]{8,}$')
# Create your models here.

class UserManager(models.Manager):
    def regvalidate(self, postData):
        errors = []
        response = {}
        salt = bcrypt.gensalt()
        password = postData['password']
        if not name_regex.match(postData['first_name']):
            errors.append('First name must be at least two characters')
        if not name_regex.match(postData['last_name']):
            errors.append('Last name must be at least two characters')
        if User.userManager.filter(email=postData['email']):
            errors.append('This e-mail address is already registered')
        if not email_regex.match(postData['email']):
            errors.append('Please enter a valid e-mail address')
        if not password_regex.match(postData['password']):
            errors.append('Your password must be at least 8 characters')
        if not postData['password'] == postData['confirmpassword']:
            errors.append('Password fields must match')

        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(first_name=postData['first_name'],last_name=postData['last_name'],email=postData['email'],password=bcrypt.hashpw(password.encode('utf-8'), salt))
        return response

    def logvalidate(self, request, email, password):
        errors = []
        loginresponse = {}
        try:
            loginemail = request.POST['loginemail']
            loginpassword = request.POST['loginpassword'].encode('utf-8')
            hashedsubmission = bcrypt.hashpw((loginpassword), bcrypt.gensalt())
            loginuser = User.userManager.filter(email=loginemail)
            hashed = loginuser[0].password.encode('utf-8')
            print hashedsubmission
            print hashed
            if bcrypt.hashpw(loginpassword, hashed) == hashed:
                loginresponse['status'] = True
                return loginresponse
            else:
                loginresponse['status'] = False
                errors.append('Your e-mail/password combination is invalid!')
                if errors:
                    loginresponse['status'] = False
                    loginresponse['errors'] = errors
                else:
                    loginresponse['status'] = True
                return loginresponse
        except (IndexError, KeyError):
            loginresponse['status'] = False
            loginresponse['errors'] = errors
            errors.append('Your e-mail address is not registered')
            return loginresponse






class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()
