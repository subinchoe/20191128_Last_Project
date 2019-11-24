from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class HashTag(models.Model):
    content = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    director = models.CharField(max_length=300)
    actor = models.CharField(max_length=300)
    score = models.FloatField()
    rating = models.CharField(max_length=50)
    audience = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    hashtags = models.ManyToManyField(HashTag, related_name='tagged_movie', blank=True)
