from django.urls import path
from . import views

app_name = "main_site"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("blog/<str:post_title>", views.blog_post, name="blog_post"),
    path("photos", views.photos, name="photos")
]