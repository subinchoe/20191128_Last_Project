from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre, HashTag
import json

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny,])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny,])
def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny,])
def hashtags(request, id):
    hashtags = HashTag.objects.filter(tagged_movie=id)
    # print(hashtags)
    movie2 = []
    # 1.각 해시태그가 있는 영화들을 value만 추출해서 movie2 한곳에 담아준다.
    for hashtag in hashtags:
        # temp = Movie.objects.filter(hashtags=hashtag)
        temp = hashtag.tagged_movie.all()
        for i in temp.values():
            if i not in movie2:
                movie2.append(i)
    # print(movie2)
    # 2.여러개 보낼 때는 serializer사용하지 않고 보내준다(리스트형태).
    return JsonResponse(movie2, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny,])
def get_genres(request):
    genres = Genre.objects.all()
    # print(genres)
    serializer = GenreSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False)
    