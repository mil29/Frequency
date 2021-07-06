from django.contrib import admin
from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<slug:slug>/', views.profile, name='profile'),
    path('create-track/<slug:slug>/', views.create_track, name='create_track'),
    path('create-instrument/<slug:slug>/<int:id>/', views.create_instrument, name='create_instrument'),
    path('track-detail/<slug:slug>/', views.track_detail, name='track_detail'),
    path('instrument-detail/<slug:slug>/<int:id>/', views.instrument_detail, name='instrument_detail'),
]
