from django.contrib import admin
from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('track-detail/<slug:slug>/', views.track_detail, name='track_detail'),
    path('profile/<slug:slug>/', views.profile, name='profile'),
    path('create-track/<slug:slug>/', views.create_track, name='create_track'),
]
