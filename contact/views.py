from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


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
    return render(request, 'contact/contact.html')
