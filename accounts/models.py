from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Genre

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
    like_genres = models.ManyToManyField(Genre, related_name='like_users')