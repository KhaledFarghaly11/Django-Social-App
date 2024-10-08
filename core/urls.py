from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload, name="upload"),
    path('follow', views.follow, name="follow"),
    path('search', views.search, name="search"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('like-post', views.like_post, name="like-post"),
    path('settings/', views.settings, name="settings"),
    path('register/', views.register, name="register"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
]
