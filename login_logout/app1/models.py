from django.db import models

# Create your models here.
class EmpModels(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    pswd=models.IntegerField()
    contact=models.IntegerField()
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.name