from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre, HashTag
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
    
@api_view(['GET'])
@permission_classes([AllowAny,])
def genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    movies = genre.movies.all().order_by('-score')
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def like(request, id):
    movie = get_object_or_404(Movie, id=id)
    user = request.user
    
    if user not in movie.users.all():
        movie.users.add(user)
        is_ok = True
    else:
        movie.users.remove(user)
        is_ok = False
    context = {
        'likes_cnt': movie.users.all().count(),
        'is_ok': is_ok
    }
    return JsonResponse(context)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def review(request, id):
    pass
