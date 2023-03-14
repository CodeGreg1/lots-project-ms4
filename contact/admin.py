from django import forms
from django.contrib import admin
from .models import ContactDetails


class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('from_name', 'message_received', 'contact_number', 'reply_to',)
    search_fields = ['from_name', 'message_received']


admin.site.register(ContactDetails, ContactDetailsAdmin)
