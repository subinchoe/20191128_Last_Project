from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, UserSerializer2
from movies.serializers import MovieSerializer, ReviewSerializer
from django.contrib.auth.forms import UserCreationForm
from .models import User
from movies.models import Movie, Review
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny,])
def signup(request):
    serializer = UserSerializer(data=request.POST)
    # print(serializer.initial_data)
    # print(serializer.errors)
    # 1.입력받은 password를 암호화하기 위해 
    if serializer.is_valid(raise_exception=True):
        password = serializer.validated_data.get('password')
        # 2.user에 원래 password를 저장하고
        user = serializer.save()
        # 3.set_password함수를 통해 암호화한 후 저장한다.
        user.set_password(raw_password=password)
        user.is_active = True
        # print(dir(user))
        user.save()
        
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def mypage(request, id):
    user = request.user
    movies = user.like_movies.all()
    serializer = MovieSerializer(movies, many=True)
    reviews = user.review_set.all()
    serializer2 = ReviewSerializer(reviews, many=True)
    serializer3 = UserSerializer2(user)
    context = {
        'user': serializer3.data,
        'movies': serializer.data,
        'reviews': serializer2.data
    }
    return JsonResponse(context, safe=False)