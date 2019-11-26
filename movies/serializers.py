from rest_framework import serializers
from .models import Genre, Movie, HashTag, Review
from accounts.models import User


class HashTagSerializer(serializers.ModelSerializer):
    # movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    class Meta:
        model = HashTag
        fields = '__all__'
        
class GenreSerializer(serializers.ModelSerializer):
    # movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')

class MovieSerializer(serializers.ModelSerializer):
    # like_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    genres = GenreSerializer(many=True)
    hashtags = HashTagSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'