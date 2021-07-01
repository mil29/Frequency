from django.contrib import admin
from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('track-detail/<slug:slug>/', views.track_detail, name='track_detail'),
]
