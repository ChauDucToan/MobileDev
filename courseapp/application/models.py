from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)