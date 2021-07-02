from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Track
from .forms import TrackCreateForm, InstrumentCreateForm, EQCreateForm
from users.models import User


@login_required
def home(request):
    user = request.user
    return render(request, 'feed/home.html')


@login_required
def profile(request, slug):
    slug = User.objects.get(slug=slug)
    u = request.user
    tracks = Track.objects.all().filter(user=u)
    context = {
        'u': u,
        'tracks': tracks,
    }
    return render(request, 'feed/profile.html', context)

    

@login_required
def track_detail(request, slug):
    u = request.user
    tracks = Track.objects.all().filter(user=u)
    context = {
        'u': u,
        'tracks': tracks,
    }
    return render(request, 'feed/track_detail.html', context)


@login_required
def create_track(request, slug):
    user = request.user
    if request.method == "POST":
        form = TrackCreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.save()
            return redirect('profile', slug=slug)
    else:
        form = TrackCreateForm()
    return render(request, 'feed/create_track.html', {'form': form })


@login_required
def create_instrument(request, slug):
    user = request.user
    if request.method == "POST":
        form = InstrumentCreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.save()
            return redirect('profile')
    else:
        form = InstrumentCreateForm()
    return render(request, 'feed/create_instrument.html', {'form': form })

@login_required
def create_eq(request, slug):
    user = request.user
    if request.method == "POST":
        form = EQCreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.save()
            return redirect('profile')
    else:
        form = EQCreateForm()
    return render(request, 'feed/create_eq.html', {'form': form })





