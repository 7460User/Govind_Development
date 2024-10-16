from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    mob=models.CharField(max_length=120)
    
    def __str__(self):
        return self.name