from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=120)
    age=models.IntegerField(max_length=30)
    email=models.CharField(max_length=120)
    contact=models.IntegerField(max_length=30)

    def __str__(self):
        return self.name