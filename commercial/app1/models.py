from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    phone = models.IntegerField(max_length=12)
    desc = models.CharField(max_length=50) 
    date = models.DateField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return  self.name
