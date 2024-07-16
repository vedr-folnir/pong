from django.contrib.auth.models import AbstractUser
from django.db import models

class Player(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, default='fallback.png')
    rank = models.IntegerField(default=1000)

    def __str__(self):
        return self.username