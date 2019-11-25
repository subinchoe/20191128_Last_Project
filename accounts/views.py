from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny,])
def signup(request):
    serializer = UserSerializer(data=request.POST)
    print(serializer.initial_data)
    # print(serializer.errors)
    if serializer.is_valid(raise_exception=True):
        password = serializer.validated_data.get('password')
        user = serializer.save()
        user.set_password(raw_password=password)
        user.save()
        
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)
