from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=30)


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=128)
    response_time = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
