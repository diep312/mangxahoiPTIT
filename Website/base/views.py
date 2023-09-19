from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def friendspage(request):
    return render(request, 'profile.html')
