from rest_framework import serializers
from .models import User
from movies.serializers import GenreSerializer

class UserSerializer(serializers.ModelSerializer):
    like_genres = GenreSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'like_genres')