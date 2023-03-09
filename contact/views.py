from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        reply_to = request.POST['reply_to']
        from_name = request.POST['from_name']
        contact_number = request.POST['contact_number']

        send_mail(
            f'LOTS Contact form filled in by {from_name}',
            f'Name:{from_name} \
            Message: {message}\
            Number: {contact_number}\
            Email: {reply_to}',
            reply_to,
            ['greg@balanced.training', ],
            fail_silently=False,
            auth_user=None,
            auth_password=None,
            connection=None,
            html_message=None,
        )
        return render(request, 'contact/contact.html', {'from_name': from_name}, )  # noqa
    else:
        return render(request, 'contact/contact.html', {},)
