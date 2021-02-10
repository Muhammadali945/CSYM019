from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

    def __str__(self):
            return f"name = {self.username} and email = {self.email}"

class Listings(models.Model):
    owner = models.CharField(max_length = 64)
    title = models.CharField(max_length=64, default="title")
    description = models.CharField(max_length=130, default="description")

    def __str__(self):
            return self.owner

