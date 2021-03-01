from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    Aadhaar_number = models.IntegerField(default = 0)
    def __str__(self):
    	return self.first_name
class Login(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    def __str__(self):
    	return self.username