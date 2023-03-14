from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactDetails
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        ContactDetails.message_received = request.POST['message_received']
        ContactDetails.reply_to = request.POST['reply_to']
        ContactDetails.from_name = request.POST['from_name']
        ContactDetails.contact_number = request.POST['contact_number']

        send_mail(
            f'LOTS Contact form filled in by {ContactDetails.from_name}',
            f'Name:{ContactDetails.from_name} \
            Message: {ContactDetails.message_received}\
            Number: {ContactDetails.contact_number}\
            Email: {ContactDetails.reply_to}',
            ContactDetails.reply_to,
            ['greg@balanced.training', ],
            fail_silently=False,
            auth_user=None,
            auth_password=None,
            html_message=None,
        )
        messages.success(request, 'Your enquiry was sent successfully.\
            Please allow a few days for a response. Thank You!')
        return render(request, 'contact/contact.html', {'from_name': ContactDetails.from_name}, )  # noqa
    else:
        return render(request, 'contact/contact.html', {},)



# from django.shortcuts import render, redirect
# from .forms import ContactForm
# from profiles.models import UserProfile

# from django.contrib import messages


# def contact(request):

#     if request.method == 'POST':
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             messages.success(request, 'Your enquiry was sent successfully. \
#                 Please allow up to 2 working days for a response.')
#             return render(request, 'contact/contact_success.html')
#         else:
#             messages.error(request, 'There was an error sending your enquiry. \
#             Please ensure all fields are valid and try again.')
#             return redirect('contact')

#     else:
#         if request.user.is_authenticated:
#             try:
#                 user = UserProfile.objects.get(user=request.user)
#                 contact_form = ContactForm(initial={
#                     'contact_name': user.default_full_name,
#                     'contact_email': user.user.email,
#                     'contact_phone_number': user.default_phone_number,
#                 })
#             except UserProfile.DoesNotExist:
#                 contact_form = ContactForm()
#         else:
#             contact_form = ContactForm()

#     template = 'contact/contact.html'
#     context = {
#         'form': contact_form,
#     }

#     return render(request, template, context)