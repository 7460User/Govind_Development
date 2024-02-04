from django.db import models

# Create your models here.
class EmpDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=101)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=50)
    zip = models.IntegerField(max_length=20)


    def __str__(self):
        return self.name