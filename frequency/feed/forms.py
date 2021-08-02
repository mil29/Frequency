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
    frequency = forms.DecimalField(label='Frequency (Hz - kHz)', widget=RangeInput(attrs={'type':'range', 'step': '1', 'value': '20', 'min': '20', 'max': '20000', 'id':'frequencyRange'}))
    boost = forms.DecimalField(label='Boost (db)', widget=RangeInput(attrs={'type':'range', 'step': '1', 'value': '0', 'min': '0', 'max': '30', 'id':'boostRange'}))
    cut   = forms.DecimalField(label='Cut (db)', widget=RangeInput(attrs={'type':'range', 'step': '1', 'value': '0', 'min': '0', 'max': '30', 'id':'cutRange'}))


    class Meta:
        model = EQ
        fields = ['description', 'frequency', 'boost', 'cut']
        widgets = {
            'description' : forms.Textarea(attrs={'rows':1, 'cols':45}),
            'description' : forms.TextInput(attrs={'placeholder': 'Enter Description'}),
        }

