from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    pwd = models.CharField(max_length=50)  # Assuming pwd is a character field
    confpwd = models.CharField(max_length=20)

    def __str__(self):
        return self.name