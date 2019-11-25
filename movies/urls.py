from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>/', views.detail),
    path('hashtags/<int:id>/', views.hashtags),
    path('genres/', views.get_genres),
]
