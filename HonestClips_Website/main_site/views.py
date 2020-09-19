from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "main_site/index.html")

def blog(request):
    return render(request, "main_site/blog.html")

def photos(request):
    return render(request, "main_site/photos.html")