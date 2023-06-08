from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
# Create your models here.

class User(AbstractBaseUser):
    name  = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    age = models.IntegerField()

    USERNAME_FIELD = 'name'
    objects = UserManager()

