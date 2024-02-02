from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    roll = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    add = models.CharField(max_length=50, null=True)




    def __str__(self):
        return self.name
