from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny,])
def index(request):
    movies = Movie.objects.all()
    print(movies)
    serializer = MovieSerializer(movies, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)