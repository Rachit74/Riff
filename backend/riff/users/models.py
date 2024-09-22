from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Client(AbstractUser):
    """
    Custom User Model (Client)
    date_joined and artist as new fields
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    artist = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def is_artist(self):
        return self.artist