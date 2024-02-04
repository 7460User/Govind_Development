from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    
class Book(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author)
 
