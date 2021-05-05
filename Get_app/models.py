from django.db import models

# Create your models here.
class Login(models.Model):
    User_name = models.CharField(max_length=500)
    Password = models.CharField(max_length=200)