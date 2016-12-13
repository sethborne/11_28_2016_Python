from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
    name = models.CharField(max_length = 50)
    description = models.OneToOneField(Description, related_name = 'course_description')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name = 'course_comment')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
