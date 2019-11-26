from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:id>/', views.mypage),
    path('signup/', views.signup),
]
