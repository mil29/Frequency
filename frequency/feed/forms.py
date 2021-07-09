from django import forms 
from .models import Instrument, EQ, Track
from feed.widgets import RangeInput



class TrackCreateForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'description', 'artist']


class InstrumentCreateForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['title']


class EQCreateForm(forms.ModelForm):
    frequency = forms.DecimalField(label='Frequency (Hz - kHz)', widget=RangeInput(attrs={'type':'range', 'step': '1' }))
    boost = forms.DecimalField(label='Boost (db)', widget=RangeInput(attrs={'type':'range', 'step': '2' }))
    cut   = forms.DecimalField(label='Cut (db)', widget=RangeInput(attrs={'type':'range', 'step': '2' }))

    class Meta:
        model = EQ
        fields = ['description', 'frequency', 'boost', 'cut']
