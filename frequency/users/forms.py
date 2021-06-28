from django import forms
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import User
=======
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

>>>>>>> 1ca64061ed8dc878427201313d0a6c544b396da6


class CustomUserCreationForm(UserCreationForm):

    class Meta:
<<<<<<< HEAD
        model = User
        fields = ['email', 'password1', 'password2']
=======
        model = CustomUser
        fields = ('username', 'email')

>>>>>>> 1ca64061ed8dc878427201313d0a6c544b396da6


class CustomUserChangeForm(UserChangeForm):

    class Meta:
<<<<<<< HEAD
        model = User      
        fields = ['email']


=======
        model = CustomUser
        fields = ('username', 'email')
>>>>>>> 1ca64061ed8dc878427201313d0a6c544b396da6
