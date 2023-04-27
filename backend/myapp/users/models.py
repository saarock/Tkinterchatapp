from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Users(models.Model):
#     name = models.CharField(max_length=120)
#     email = models.EmailField()
#     password = models.CharField(max_length=300)
#     repassword = models.CharField(max_length=300)

#     def __str__(self):
#         return self.name



class Messages(models.Model):
    sender = models.CharField(max_length=120)
    message = models.TextField(max_length=1000)
