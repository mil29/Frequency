from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Track


@login_required
def home(request):
    return render(request, 'feed/home.html')


@login_required
def track_detail(request, slug):
    return render(request, 'track_detail', {
        'track': get_object_or_404(Track, slug=slug)
    })


@login_required
def profile(request)

