from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index),
    path('top10/', views.top10),
    path('<int:id>/', views.recommended),
    path('detail/<int:id>/', views.detail),
    path('hashtag/<int:id>/', views.get_movies),
    path('hashtags/<int:id>/', views.hashtags),
    path('genres/', views.get_genres),
    path('genre/<int:id>/', views.genre),
    path('<int:id>/like/', views.like),
    path('<int:id>/reviews/', views.get_reviews),
    path('<int:id>/review/', views.review),
    path('sorts/', views.sorts),
    path('sort/<int:sort>/<int:id>/', views.sort)
]
