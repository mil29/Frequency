from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import User, Profile


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text="Minimum of 8 characters")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
  

    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User      
        fields = ['email']


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = Profile      
        fields = ['bio', 'pic']

