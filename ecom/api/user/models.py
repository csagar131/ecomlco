from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length = 50, default = 'Anonymous')
    email = models.EmailField(unique = True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.IntegerField(blank = True, null = True)
    gender = models.CharField(max_length = 10 ,blank = True, null = True)

    session_token =  models.CharField(max_length = 10, default = '0')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
