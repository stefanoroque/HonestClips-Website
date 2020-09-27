from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2

# Create your views here.

def index(request):
    return render(request, "main_site/index.html")

def blog(request):
    # Find all current blog_posts
    return render(request, "main_site/blog.html")

def blog_post(request, post_title):
    post = util.get_post(post_title)
    
    return render(request, "main_site/blog_post.html", {
            "post": markdown2.markdown(post),
            "post_title": post_title
        })

def photos(request):
    return render(request, "main_site/photos.html")

def location_photos(request, location):
    # Find all photos (file_names) from that location
    all_photos = util.get_photos(location)

    return render(request, "main_site/location_photos.html", {
            "location": location,
            "file_names": all_photos
        })
