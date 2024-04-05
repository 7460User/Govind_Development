from django.db import models

# Create your models here.
class student_Data(models.Model):
    name=models.CharField(max_length=30)
    school=models.CharField(max_length=120)
    roll=models.IntegerField(max_length=10)
    contact=models.IntegerField(max_length=10)

    def __str__(self):
        return self.name