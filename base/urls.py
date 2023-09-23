from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginandregister, name='loginandregister'),
    path('home/', views.home, name='homepage'),
    path('profile/<str:pk>/', views.friendspage, name='profile'),
]