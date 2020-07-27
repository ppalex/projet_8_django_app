from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser,models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.username