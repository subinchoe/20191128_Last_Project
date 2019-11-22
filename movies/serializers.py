from rest_framework import serializers
from .models import Genre, Movie, HashTag
from accounts.models import User

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    like_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    hashtags = serializers.PrimaryKeyRelatedField(queryset=HashTag.objects.all(), many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'image', 'director', 'actor', 'score', 'rating', 'genres', 'like_users', 'hashtags')

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    like_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies', 'like_users')

class HashTagSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = HashTag
        fields = ('id', 'content', 'movies')