from django import forms 
from .models import Instrument, EQ, Track



class TrackCreateForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'description', 'artist']


class InstrumentCreateForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['title']


class EQCreateForm(forms.ModelForm):
    class Meta:
        model = EQ
        fields = ['frequency', 'boost', 'cut']

