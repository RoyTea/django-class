import email
from unicodedata import name
from django.db import models

# Department Models


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3) 
    course = models.CharField(max_length=15)
    insname = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    


