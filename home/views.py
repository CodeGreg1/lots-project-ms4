from django.shortcuts import render
from django.contrib.staticfiles import storage


# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, "home/index.html")
