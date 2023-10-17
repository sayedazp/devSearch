from django.shortcuts import render
from .models import Profile
# Create your views here.

def users(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/users.html', context)

def userProfile(request, pk):
    prof = Profile.objects.get(id = pk)
    context = {'profile':prof}
    return render(request, 'users/user-profile.html', context)