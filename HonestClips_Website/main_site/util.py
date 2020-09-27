import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_posts():
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("blog_posts")
    return list(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md"))


def get_post(title):
    """
    Retrieves a blog post by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"blog_posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def get_photos(location_name):
    """
    Returns a list of the filenames of all the photos from a specific location.
    """
    _, filenames = default_storage.listdir("main_site/static/main_site/imgs/" + location_name)
    return filenames
    # return list(re.sub(r"\.jpeg$", "", filename)
    #             for filename in filenames if filename.endswith(".jpeg"))
