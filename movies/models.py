from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class HashTag(models.Model):
    content = models.CharField(max_length=100)
    def __str__(self):
        return self.content

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    description = models.TextField()
    director = models.CharField(max_length=300)
    actor = models.CharField(max_length=300)
    score = models.FloatField()
    rating = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_year = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    hashtags = models.ManyToManyField(HashTag, related_name='tagged_movie', blank=True)
    video = models.CharField(max_length=400, blank=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    star = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class Sort(models.Model):
    sort = models.IntegerField()
    name = models.CharField(max_length=100)
    hashtags = models.ManyToManyField(HashTag, related_name='sorted_name', blank=True)
    def __str__(self):
        return self.name