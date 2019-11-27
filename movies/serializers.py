from rest_framework import serializers
from .models import Genre, Movie, HashTag, Review, Sort
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

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

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M")
    class Meta:
        model = Review
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'star', )

class MovieSerializer(serializers.ModelSerializer):
    # users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    genres = GenreSerializer(many=True)
    hashtags = HashTagSerializer(many=True)
    class Meta:
        model = Movie
        fields ='__all__'

class SortSerializer(serializers.ModelSerializer):
    hashtags = HashTagSerializer(many=True)
    class Meta:
        model = Sort
        fields = '__all__'