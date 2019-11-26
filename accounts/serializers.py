from rest_framework import serializers
from .models import User
from movies.serializers import GenreSerializer

class UserSerializer(serializers.ModelSerializer):
    # like_genres = GenreSerializer(many=True) 안써줘야함
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
                'like_genres': {
                    # Tell DRF that the link field is not required.
                    'required': False,
                }
            }
