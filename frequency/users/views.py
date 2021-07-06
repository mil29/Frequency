from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, User

def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = CustomUserCreationForm()
	return render (request=request, template_name="users/register.html", context={"form":form})

@login_required
def create_profile(request, slug):
	u = request.user
	if request.method == "POST":
		form = ProfileCreationForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.user_profile = u
			data.save()
			messages.success(request, "Profile Updated.")
			return redirect("profile", slug=slug)
		messages.error(request, "Unsuccessful update. Invalid information.")
	else:
		form = ProfileCreationForm()
	return render (request=request, template_name="users/create_profile.html", context={"form":form})


@login_required
def update_profile(request, slug):
	u = request.user
	profile = Profile.objects.get(user_profile=u)
	if request.method == "POST":
		form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			data = form.save(commit=False)
			data.user_profile = u
			data.save()
			messages.success(request, "Profile Updated.")
			return redirect("profile", slug=slug)
		messages.error(request, "Unsuccessful update. Invalid information.")
	else:
		form = ProfileCreationForm(instance=profile)
	return render (request=request, template_name="users/create_profile.html", context={"form":form})
	
