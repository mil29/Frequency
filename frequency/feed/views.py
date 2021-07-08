from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Track, Instrument, EQ
from .forms import TrackCreateForm, InstrumentCreateForm, EQCreateForm
from users.models import User, Profile
from django.urls import reverse


@login_required
def home(request):
    user = request.user
    return render(request, 'feed/home.html')


@login_required
def profile(request, slug):
    slug = User.objects.get(slug=slug)
    u = request.user
    tracks = Track.objects.all().filter(user=u)
    profile = Profile.objects.all().filter(user_profile=u)
    context = {
        'u': u,
        'tracks': tracks,
        'profile': profile,
    }
    return render(request, 'feed/profile.html', context)

    

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
def create_instrument(request, track_slug, id):
    user = request.user
    track = get_object_or_404(Track, id=id)
    if request.method == "POST":
        form = InstrumentCreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.artist = user
            data.track = track
            data.save()
            return redirect('instrument_detail', track_slug=track.slug, id=track.id)
    else:
        form = InstrumentCreateForm()
    return render(request, 'feed/create_instrument.html', {'form': form })

@login_required
def create_eq(request, track_slug, instrument_slug, id):
    user = request.user
    instrument = get_object_or_404(Instrument, id=id)
    if request.method == "POST":
        form = EQCreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.instrument = instrument
            data.track = instrument.track
            data.save()
            return redirect('eq_detail', track_slug=instrument.track.slug, instrument_slug=instrument.slug, id=instrument.id)
    else:
        form = EQCreateForm()
    return render(request, 'feed/create_eq.html', {'form': form })


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
def instrument_detail(request, track_slug, id):
    user = request.user
    track = get_object_or_404(Track, id=id)
    my_inst = Instrument.objects.filter(track_id=track.id)
    if my_inst.exists():
        context = {
            'instruments': my_inst,
            'track': track,
        }
        return render(request, 'feed/instrument_detail.html', context)
    else:
        print('There are no instruments set in your track')
        return redirect('create_instrument', track_slug=track.slug, id=track.id)


@login_required
def eq_detail(request, track_slug, instrument_slug, id):
    user = request.user
    instrument = get_object_or_404(Instrument, id=id)
    eqs = EQ.objects.filter(instrument_id=instrument.id)
    if eqs.exists():
        context = {
            'instrument': instrument,
            'eqs': eqs,
        }
        return render(request, 'feed/eq_detail.html', context)
    else:
        return redirect('create_eq', track_slug=instrument.track.slug, instrument_slug=instrument.slug, id=instrument.id)

