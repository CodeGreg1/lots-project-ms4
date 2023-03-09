from django.shortcuts import render
from django.contrib.staticfiles import storage
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, "home/index.html")


def about_us(request):
    """ A view to return the index page """
    return render(request, "home/about_us.html")


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['reply_to']
        name = request.POST['from_name']
        number = request.POST['contact_number']

        send_mail(
            f'LOTS Contact form filled in by {name}',
            f'Name:{name} \
            Message: {message}\
            Number: {number}\
            Email: {email}',
            email,
            [settings.EMAIL_HOST_USER, ],
            fail_silently=False,
        )
        return render(request, 'home/contact.html')
    else:
        return render(request, 'home/contact.html')


# @csrf_exempt
# def contact_us(request):
#     """ A view to return the index page """
#     return render(request, "home/contact_us.html")


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


def admin(request):
    """ A view to return the admin page """
    return render(request, "admin/")


def add_post(request):
    """ A view to return the admin page """
    return render(request, "admin/news/post/add/")


def LUk(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/lbm-uk.html")


def TUk(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/tlb-uk.html")


def TLUk(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/tlb-lbm-uk.html")


def TLEu(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/tlb-lbm-europe.html")


def TEu(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/tlb-europe.html")


def LEu(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/lbm-europe.html")


def TLWorld(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/tlb-lbm-world.html")


def TWorld(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/tlb-world.html")


def LWorld(request):
    """ A view to return the Payment page """
    return render(request, "home/membership-type/lbm-world.html")
