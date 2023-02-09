from django.shortcuts import render
from django.contrib.staticfiles import storage


# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, "home/index.html")


def about_us(request):
    """ A view to return the index page """
    return render(request, "home/about_us.html")


def links(request):
    """ A view to return the links page """
    return render(request, "home/links.html")


def membership(request):
    """ A view to return the membership page """
    return render(request, "home/membership.html")


def publications(request):
    """ A view to return the publications page """
    return render(request, "home/publications.html")


def sales(request):
    """ A view to return the sales page """
    return render(request, "home/sales.html")


def news(request):
    """ A view to return the news page """
    return render(request, "home/news.html")
