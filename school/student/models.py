from django.db import models

# Create your models here.
class Student(models.Model):
    regno= models.IntegerField()
    fullname= models.CharField(max_length=30)
    department= models.CharField(max_length=15)
    phone_number= models.CharField(max_length=11)
    email= models.EmailField(blank=True, null=True)
    dob= models.DateField(default=True)
    is_nigerian= models.BooleanField(default=True)

    def __str__(self):
       return self.fullname