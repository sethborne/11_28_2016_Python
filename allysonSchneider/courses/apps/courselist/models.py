from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
