from django.shortcuts import render
from django.contrib.staticfiles import storage


# Create your views here.
def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, "bag/bag.html")

