from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Track, Instrument, EQ
from .forms import TrackCreateForm, InstrumentCreateForm, EQCreateForm
from users.models import User, Profile
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from collections import Counter

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
    eq_boost_all = EQ.objects.filter(track_id=track.id)
    track_boost = eq_boost_all.aggregate(Sum('boost'))
    track_cut = eq_boost_all.aggregate(Sum('cut'))


    # Look at eq_detail view for more info on the code below , this code extracts the occurrence of certain frequencies 
    f = 1
    a = -10000
    b = 25000
    d = [x * f for x in range(a,b,100)]

    frequencies = EQ.objects.filter(track_id=track.id).values_list('frequency', flat=True)

    clashing_freq = []
    for num in d:
        for freq in frequencies:
            x = num - 50
            y = num + 50
            if freq in range(x, y) and num != 0:
                clashing_freq.append(num)
            continue
    clashCounter = Counter(clashing_freq)

    clashTrackFreq = []
    clashTrackNo = []
    for key, value in clashCounter.items():
        if value > 1:
            clashTrackFreq.append(key)
            clashTrackNo.append(value)


    if my_inst.exists():
        context = {
            'instruments': my_inst,
            'track': track,
            'track_boost': track_boost,
            'track_cut': track_cut,
            'clashTrackFreq': clashTrackFreq,
            'clashTrackNo': clashTrackNo,
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
    inst_boost = eqs.aggregate(Sum('boost'))
    inst_cut = eqs.aggregate(Sum('cut'))


    # code to find a build up of frequencies in a certain range 

    # this code below sets a range in a and b and the in d loops through the range every 50 and creates a list in d
    f = 1
    a = -10000
    b = 25000
    d = [x * f for x in range(a,b,100)]
    # print(d)

    #  this will find the frequency entries within the model for a particular instrument a give a back a list
    frequencies = EQ.objects.filter(instrument_id=instrument.id).values_list('frequency', flat=True)
    
    #  this loops through the list above called d which is a large range of numbers spaced by 50 and also loops through the frequency entries in the model for the instrument checks whether the entry is within a range of 50 and adds to list called clashing_freq , the the counter counts the number of times a entry comes up in the list 'clashCounter'
    clashing_freq = []
    for num in d:
        for freq in frequencies:
            x = num - 50
            y = num + 50
            if freq in range(x, y) and num != 0:
                clashing_freq.append(num)
            continue
    # print(clashing_freq)
    clashCounter = Counter(clashing_freq)
    # print(clashCounter)

    #  this adds the key and values into seperate lists from the classCounter dictionary above
    clashFreq = []
    clashNo = []
    for key, value in clashCounter.items():
        if value > 1:
            clashFreq.append(key)
            clashNo.append(value)


    if eqs.exists():
        context = {
            'instrument': instrument,
            'eqs': eqs,
            'inst_boost': inst_boost,
            'inst_cut': inst_cut,
            'clashFreq': clashFreq,
            'clashNo': clashNo,
        }
        return render(request, 'feed/eq_detail.html', context)
    else:
        return redirect('create_eq', track_slug=instrument.track.slug, instrument_slug=instrument.slug, id=instrument.id)


@login_required
def eq_delete(request, id):
    eq_obj = get_object_or_404(EQ, id=id)
    eq_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def instrument_delete(request, id):
    inst_obj = get_object_or_404(Instrument, id=id)
    inst_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def track_delete(request, id):
    inst_obj = get_object_or_404(Track, id=id)
    inst_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

